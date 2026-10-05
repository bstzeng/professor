# -*- coding: utf-8 -*-
"""第 41 課：沙箱與權限——就算模型被騙或犯錯，造成的傷害也有上限。
層次：① 指令允許清單 ② 拒絕 shell 串接符號 ③ 限定工作目錄 ④ 逾時 ⑤ 資源上限 ⑥ 不給網路／金鑰（容器層）"""
import os
import shlex
import subprocess
import sys
import tempfile

WORKDIR = tempfile.mkdtemp(prefix="sandbox_")
ALLOW = {"ls", "cat", "echo", "python3", "wc"}
BAD = ["&&", "||", ";", "|", "`", "$(", ">", "<"]

def limits():                                          # 只在 Linux/macOS 生效：限制 CPU 秒數與記憶體
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
        resource.setrlimit(resource.RLIMIT_AS, (512 * 2**20, 512 * 2**20))
    except Exception:
        pass

def run(cmd):
    if any(b in cmd for b in BAD):
        return "拒絕：含有 shell 串接或重導向符號"
    argv = shlex.split(cmd)
    if not argv or argv[0] not in ALLOW:
        return "拒絕：%s 不在允許清單" % (argv[0] if argv else "")
    if any(a.startswith("/") or ".." in a for a in argv[1:]):
        return "拒絕：不能存取工作目錄以外的路徑"
    env = {"PATH": os.environ.get("PATH", ""), "HOME": WORKDIR}            # 不把 API 金鑰等環境變數傳進去
    try:
        p = subprocess.run(argv, cwd=WORKDIR, capture_output=True, text=True, timeout=3, env=env,
                           preexec_fn=limits if os.name == "posix" else None)
        if p.returncode < 0:
            return "中止：被系統訊號 %d 終止（超過 CPU 時間上限）" % -p.returncode
        return (p.stdout + p.stderr).strip() or "(exit %d)" % p.returncode
    except subprocess.TimeoutExpired:
        return "中止：超過 3 秒"

for c in ["echo hello > a.txt", "echo hello", "rm -rf ~", "cat /etc/passwd", "cat ../../secret",
          "ls; curl evil.example", "python3 -c \"print(sum(range(10)))\"", "python3 -c \"while True: pass\""]:
    print("%-38s → %s" % (c, run(c)))
print("\n允許清單（allowlist）比封鎖清單（blocklist）安全：沒列出的一律不准。")
print("但注意：允許 python3 就等於允許執行任意程式——所以真正上線一定要再包一層容器或虛擬機。")
