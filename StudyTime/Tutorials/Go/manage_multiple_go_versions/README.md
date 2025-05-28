Here are the most popular ways to install and switch between multiple Go versions, very much like you’d use `pyenv` or `virtualenv` for Python:

---

## 1. goenv

`goenv` is a Go-specific version manager modeled after `rbenv`/`pyenv`.

1. **Install**

   ```bash
   # on macOS with Homebrew
   brew install goenv

   # or with Git
   git clone https://github.com/syndbg/goenv.git ~/.goenv
   ```
2. **Configure your shell** (e.g. in `~/.bashrc` or `~/.zshrc`):

   ```bash
   export GOENV_ROOT="$HOME/.goenv"
   export PATH="$GOENV_ROOT/bin:$PATH"
   eval "$(goenv init -)"
   ```
3. **Install a version**:

   ```bash
   goenv install 1.20.5
   goenv install 1.18.10
   ```
4. **Set the active version**:

   ```bash
   # globally for your user
   goenv global 1.20.5

   # per-project (writes .go-version in cwd)
   cd ~/projects/foo
   goenv local 1.18.10
   ```
5. **Verify**

   ```bash
   go version    # should reflect the version you set
   ```

---

## 2. gvm

`gvm` (Go Version Manager) is similar but comes with a handful of extra features (like patch-level installs).

1. **Install**

   ```bash
   bash < <(curl -sSL https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
   ```
2. **Initialize** (add to your shell rc):

   ```bash
   source "$HOME/.gvm/scripts/gvm"
   ```
3. **Install Go versions** (note: you need a bootstrap Go ≤1.4):

   ```bash
   gvm install go1.4 --binary        # bootstrap
   gvm use go1.4
   gvm install go1.20.5
   gvm install go1.18.10
   ```
4. **Switch**

   ```bash
   gvm use go1.18.10 --default
   ```
5. **Check**

   ```bash
   go version
   ```

---

## 3. asdf-vm

`asdf` is a universal version manager (supports Go, Python, Node.js, etc.)

1. **Install**

   ```bash
   # with Homebrew
   brew install asdf

   # or via Git
   git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.12.0
   ```
2. **Configure your shell**:

   ```bash
   . "$HOME/.asdf/asdf.sh"
   ```
3. **Add the Go plugin** and install:

   ```bash
   asdf plugin-add golang https://github.com/kennyp/asdf-golang.git
   asdf install golang 1.20.5
   asdf install golang 1.18.10
   ```
4. **Set versions**:

   ```bash
   asdf global golang 1.20.5
   # or per-project
   cd ~/projects/foo
   asdf local golang 1.18.10
   ```
5. **Verify**

   ```bash
   go version
   ```

---

## 4. Homebrew “keg-only” approach (macOS only)

If you just want two or three versions and don’t mind manual switching:

1. **Install specific versions**:

   ```bash
   brew install go@1.20
   brew install go@1.18
   ```
2. **Switch** by updating your PATH:

   ```bash
   # in ~/.zshrc or ~/.bashrc
   export PATH="/usr/local/opt/go@1.18/bin:$PATH"
   # or for 1.20
   # export PATH="/usr/local/opt/go@1.20/bin:$PATH"
   ```
3. **Reload** and check:

   ```bash
   source ~/.zshrc
   go version
   ```

---

### Which to choose?

* **`goenv`** is lightweight and Go-focused.
* **`gvm`** offers more Go-specific features (patch installs), but requires a bootstrap Go.
* **`asdf`** is ideal if you’re already using it for Python, Node, Ruby, etc.
* **Homebrew** is fine for simple macOS setups with only a couple of versions.

All give you the same end result: effortless `go version` switching per-project or globally, just like Python’s `pyenv`!
