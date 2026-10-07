# -*- coding: utf-8 -*-
"""〈GitHub 從零到協作〉的 Git 指令範例：每個範例在隔離的沙盒中實際執行，輸出存成 gh_ex_out.json。

執行：python3 gh_examples.py
每個範例 = (隱藏的準備指令, 顯示的指令列表)。日期固定，所以 commit 雜湊每次都一樣。
「origin」是本機的裸倉庫（bare repository），用來模擬 GitHub 上的遠端倉庫。
"""
import io
import json
import os
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "gh_ex_out.json")

# 共用的準備：一個已有兩個 commit 的專案 demo
BASE = """
mkdir demo && cd demo && git init -q
printf '# 我的專案\\n' > README.md
git add README.md && git commit -q -m "初始提交：加入 README"
printf 'print("hello")\\n' > app.py
git add app.py && git commit -q -m "加入 app.py"
"""

# 共用的準備：GitHub 上的遠端倉庫（裸倉庫）
REMOTE = """
git init -q --bare github/ming/demo.git
git clone -q github/ming/demo.git seed 2>/dev/null; cd seed
printf '# demo\\n' > README.md
git add README.md && git commit -q -m "Initial commit"
git push -q origin main
cd ..
"""

EX = {
  "config": ("", [
    'git config --global user.name "Ming Chen"',
    'git config --global user.email "ming@example.com"',
    'git config --global init.defaultBranch main',
    'git config --global --list',
  ]),
  "init": ("", [
    'mkdir demo',
    'cd demo',
    'git init',
    'ls -a',
    'git status',
  ]),
  "first": ("mkdir demo && cd demo && git init -q", [
    "printf '# 我的專案\\n' > README.md",
    'git status',
    'git add README.md',
    'git status',
    'git commit -m "初始提交：加入 README"',
    'git log',
  ]),
  "diff": (BASE, [
    "printf 'print(\"hello\")\\nprint(\"world\")\\n' > app.py",
    'git status --short',
    'git diff',
    'git add app.py',
    'git diff',
    'git diff --staged',
    'git commit -q -m "app.py 多印一行"',
  ]),
  "log": (BASE + """
printf 'print("hello")\\nprint("world")\\n' > app.py
git commit -q -am "app.py 多印一行"
""", [
    'git log --oneline',
    'git log --oneline --stat -1',
    'git show HEAD',
    'git log --oneline -- README.md',
  ]),
  "ignore": (BASE, [
    "mkdir -p build logs && touch build/out.bin logs/a.log .env notes.txt",
    'git status --short',
    "printf 'build/\\n*.log\\n.env\\n' > .gitignore",
    'git status --short',
    'git check-ignore -v logs/a.log .env',
    'git add .gitignore notes.txt && git commit -q -m "加入 .gitignore"',
  ]),
  "restore": (BASE, [
    "printf 'oops\\n' > app.py",
    'git status --short',
    'git restore app.py',
    'cat app.py',
    "printf 'print(\"v2\")\\n' > app.py && git add app.py",
    'git status --short',
    'git restore --staged app.py',
    'git status --short',
  ]),
  "reset": (BASE + """
printf 'print("bug")\\n' > app.py
git commit -q -am "不小心加入的 bug"
""", [
    'git log --oneline',
    'git revert --no-edit HEAD',
    'git log --oneline',
    'git reset --hard HEAD~2',
    'git log --oneline',
  ]),
  "reset3": (BASE + """
printf 'print("v3")\\n' > app.py
git commit -q -am "第三個 commit"
""", [
    'git reset --soft HEAD~1',
    'git status --short',
    'git commit -q -m "重新提交"',
    'git reset --mixed HEAD~1',
    'git status --short',
    'git reset --hard',
    'git status --short',
    'git log --oneline',
  ]),
  "amend": (BASE, [
    "printf 'MIT\\n' > LICENSE",
    'git add LICENSE && git commit -q -m "加入授全條款"',
    'git log --oneline -1',
    'git commit --amend -m "加入授權條款"',
    'git log --oneline',
  ]),
  "stash": (BASE, [
    "printf 'print(\"寫到一半\")\\n' >> app.py",
    'git stash push -m "功能寫到一半"',
    'git status --short',
    'git stash list',
    'git stash pop',
    'git status --short',
  ]),
  "tag": (BASE, [
    'git tag -a v1.0.0 -m "第一個正式版"',
    "printf 'print(\"v1.1\")\\n' > app.py && git commit -q -am \"小修正\"",
    'git tag',
    'git describe --tags',
    'git show v1.0.0 --stat',
  ]),
  "branch": (BASE, [
    'git branch',
    'git switch -c feature-login',
    "printf 'def login(): pass\\n' > login.py",
    'git add login.py && git commit -q -m "加入登入功能"',
    'git branch -v',
    'git switch main',
    'ls',
    'git log --oneline --all --graph',
  ]),
  "ffmerge": (BASE + """
git switch -q -c feature-login
printf 'def login(): pass\\n' > login.py
git add login.py && git commit -q -m "加入登入功能"
git switch -q main
""", [
    'git merge feature-login',
    'git log --oneline --graph',
    'git branch -d feature-login',
  ]),
  "merge3": (BASE + """
git switch -q -c feature-login
printf 'def login(): pass\\n' > login.py
git add login.py && git commit -q -m "加入登入功能"
git switch -q main
printf '# 我的專案\\n\\n一個小工具。\\n' > README.md
git commit -q -am "README 加上說明"
""", [
    'git log --oneline --graph --all',
    'git merge --no-edit feature-login',
    'git log --oneline --graph',
  ]),
  "conflict": (BASE + """
git switch -q -c feature-greet
printf 'print("你好")\\n' > app.py
git commit -q -am "改成中文問候"
git switch -q main
printf 'print("Hello!")\\n' > app.py
git commit -q -am "問候加上驚嘆號"
""", [
    'git merge feature-greet',
    'git status',
    'cat app.py',
    "printf 'print(\"你好！\")\\n' > app.py",
    'git add app.py',
    'git commit --no-edit',
    'git log --oneline --graph',
  ]),
  "rebase": (BASE + """
git switch -q -c feature-login
printf 'def login(): pass\\n' > login.py
git add login.py && git commit -q -m "加入登入功能"
printf 'def logout(): pass\\n' >> login.py
git commit -q -am "加入登出功能"
git switch -q main
printf '# 我的專案\\n\\n一個小工具。\\n' > README.md
git commit -q -am "README 加上說明"
git switch -q feature-login
""", [
    'git log --oneline --graph --all',
    'git rebase main',
    'git log --oneline --graph --all',
  ]),
  "squash": (BASE + """
git switch -q -c feature-login
printf 'def login(): pass\\n' > login.py
git add login.py && git commit -q -m "加入登入功能"
printf 'def logout(): pass\\n' >> login.py
git commit -q -am "加入登出功能"
printf '# typo fixed\\n' >> login.py
git commit -q -am "修錯字"
git switch -q main
""", [
    'git merge --squash feature-login',
    'git commit -q -m "登入與登出功能 (#12)"',
    'git log --oneline --graph',
  ]),
  "cherry": (BASE + """
git switch -q -c experiment
printf 'def helper(): pass\\n' > util.py
git add util.py && git commit -q -m "加入 util.py 小工具"
printf 'print("實驗")\\n' > app.py
git commit -q -am "實驗性修改"
git switch -q main
""", [
    'git log --oneline experiment',
    'git cherry-pick experiment~1',
    'git log --oneline',
  ]),
  "reflog": (BASE + """
printf 'print("重要的工作")\\n' > app.py
git commit -q -am "重要的工作"
""", [
    'git reset --hard HEAD~1',
    'git log --oneline',
    'git reflog',
    'git reset --hard HEAD@{1}',
    'git log --oneline',
  ]),
  "remote": (REMOTE, [
    'git clone github/ming/demo.git demo',
    'cd demo',
    'git remote -v',
    "printf 'print(\"hello\")\\n' > app.py",
    'git add app.py && git commit -q -m "加入 app.py"',
    'git status',
    'git push',
    'git status',
  ]),
  "pull": (REMOTE + """
git clone -q github/ming/demo.git laptop
git clone -q github/ming/demo.git desktop
cd desktop
printf 'print("在桌機寫的")\\n' > app.py
git add app.py && git commit -q -m "桌機：加入 app.py"
git push -q
cd ../laptop
""", [
    'git fetch',
    'git status',
    'git log --oneline --all',
    'git pull',
    'git log --oneline',
  ]),
  "pushrej": (REMOTE + """
git clone -q github/ming/demo.git laptop
git clone -q github/ming/demo.git desktop
cd desktop
printf 'print("桌機")\\n' > app.py
git add app.py && git commit -q -m "桌機的修改"
git push -q
cd ../laptop
git config pull.rebase true
printf 'MIT\\n' > LICENSE
git add LICENSE && git commit -q -m "筆電：加入 LICENSE"
""", [
    'git push',
    'git pull',
    'git log --oneline --graph',
    'git push',
  ]),
  "newbranch_push": (REMOTE + """
git clone -q github/ming/demo.git demo
cd demo
""", [
    'git switch -c fix-typo',
    "printf '# demo 專案\\n' > README.md",
    'git commit -q -am "修正 README 標題"',
    'git push -u origin fix-typo',
    'git branch -vv',
  ]),
  "upstream": ("""
git init -q --bare github/torvalds/tool.git
git clone -q github/torvalds/tool.git seed 2>/dev/null; cd seed
printf '# tool\\n' > README.md && git add README.md && git commit -q -m "Initial commit" && git push -q origin main
cd ..
git clone -q --bare github/torvalds/tool.git github/ming/tool.git
git clone -q github/ming/tool.git tool
cd seed
printf 'v2\\n' > VERSION && git add VERSION && git commit -q -m "原專案：發布 v2" && git push -q
cd ../tool
""", [
    'git remote -v',
    'git remote add upstream ../github/torvalds/tool.git',
    'git fetch upstream',
    'git merge upstream/main',
    'git push origin main',
  ]),
  "objects": (BASE, [
    'git cat-file -t HEAD',
    'git cat-file -p HEAD',
    'git cat-file -p "HEAD^{tree}"',
    'git cat-file -p HEAD:README.md',
    "printf '# 我的專案\\n' | git hash-object --stdin",
    'git rev-parse HEAD:README.md',
  ]),
  "refs": (BASE + "git switch -q -c dev && git switch -q main", [
    'ls .git',
    'cat .git/HEAD',
    'ls .git/refs/heads',
    'cat .git/refs/heads/main',
    'git rev-parse main dev HEAD',
    'git switch -q dev && cat .git/HEAD',
  ]),
  "pack": (BASE + """
for i in 1 2 3 4 5 6 7 8; do printf 'line %s\\n' $i >> app.py; git commit -q -am "修改 $i"; done
""", [
    'git count-objects -v',
    'git gc --quiet',
    'git count-objects -v',
    'ls .git/objects/pack',
  ]),
  "secret": (BASE + """
printf 'API_KEY=sk-test-123\\n' > .env
git add .env && git commit -q -m "加入設定"
""", [
    'git log --oneline --stat -1',
    'git rm --cached .env',
    "printf '.env\\n' >> .gitignore",
    'git add .gitignore && git commit -q -m "停止追蹤 .env"',
    'git status --short --ignored',
    'git log --oneline --all -- .env',
  ]),
  "wrongbranch": (BASE, [
    "printf 'def pay(): pass\\n' > pay.py && git add pay.py && git commit -q -m \"加入付款功能\"",
    'git branch feature-pay',
    'git reset --hard HEAD~1',
    'git switch feature-pay',
    'git log --oneline --graph --all',
  ]),
  "bisect": (BASE + """
for i in 1 2 3 4 5 6; do
  if [ $i -eq 4 ]; then printf 'print(1/0)\\n' >> app.py; else printf '# v%s\\n' $i >> app.py; fi
  git commit -q -am "第 $i 版"
done
""", [
    'git log --oneline',
    'git bisect start HEAD HEAD~6',
    'git bisect run python3 app.py',
    'git bisect reset',
  ]),
  "blame": (BASE + """
printf 'print("hello")\\nprint("world")\\n' > app.py
GIT_AUTHOR_NAME="Hua Lin" GIT_AUTHOR_EMAIL="hua@example.com" git commit -q -am "多印一行"
""", [
    'git blame app.py',
  ]),
}

ORDER = list(EX.keys())


def run_one(name, setup, cmds, root):
    d = os.path.join(root, name)
    os.makedirs(os.path.join(d, "home"))
    with io.open(os.path.join(d, "home", ".gitconfig"), "w", encoding="utf-8") as f:
        if name != "config":
            f.write(u"[user]\n\tname = Ming Chen\n\temail = ming@example.com\n[init]\n\tdefaultBranch = main\n[core]\n\tpager = cat\n[advice]\n\tdetachedHead = false\n")
    lines = ["exec 2>&1", "t=0", "tick(){ t=$((t+1)); export GIT_AUTHOR_DATE=\"2026-03-01T10:$(printf %02d $t):00+08:00\"; export GIT_COMMITTER_DATE=\"$GIT_AUTHOR_DATE\"; }",
             "git(){ tick; command git \"$@\"; }"]
    lines += [l for l in setup.strip().split("\n") if l.strip()]
    for i, c in enumerate(cmds):
        lines.append("echo '@@CMD %d'" % i)
        lines.append(c)
    env = {"GIT_PAGER": "cat", "HOME": os.path.join(d, "home"), "PATH": os.environ["PATH"], "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "GIT_PAGER": "cat", "TERM": "dumb",
           "GIT_CONFIG_NOSYSTEM": "1", "EDITOR": "true"}
    r = subprocess.run(["bash", "-c", "\n".join(lines)], cwd=d, env=env, stdout=subprocess.PIPE, timeout=60)
    out = r.stdout.decode("utf-8")
    parts = out.split("@@CMD ")
    res = []
    for p in parts[1:]:
        k, _, body = p.partition("\n")
        body = body.replace(d + "/", "/home/ming/").replace(d, "/home/ming")
        body = "\n".join(l.split("\r")[-1].strip() if "\r" in l else l for l in body.split("\n"))
        res.append([cmds[int(k)], body.rstrip("\n")])
    pre = parts[0].strip()
    if pre:
        raise SystemExit("%s: setup produced output:\n%s" % (name, pre))
    return res


def run():
    root = tempfile.mkdtemp(prefix="ghex")
    out = {}
    try:
        for n in ORDER:
            s, c = EX[n]
            out[n] = run_one(n, s, c, root)
    finally:
        shutil.rmtree(root)
    with io.open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    o = run()
    for n in ORDER:
        print("=" * 20, n)
        for c, b in o[n]:
            print("$ " + c)
            if b:
                print(b)
