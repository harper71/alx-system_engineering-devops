The `whoami` command in Linux is a simple and useful command that displays the current user logged into the system. It effectively tells you "who am I" in terms of the logged-in user.

### How to Use `whoami`

1. **Open Terminal**

    Open your terminal application.

2. **Run the `whoami` Command**

    Simply type `whoami` and press Enter.

    ```bash
    whoami
    ```

    Example output:

    ```plaintext
    ubuntu
    ```

    This will display the username of the current user.

### Practical Examples

#### Example 1: Checking the Current User

```bash
whoami
```

Output:

```plaintext
ubuntu
```

This output indicates that the current user is `ubuntu`.

#### Example 2: Using `whoami` in Scripts

You can use `whoami` in shell scripts to get the current user and perform actions based on the user. Here's a simple example:

```bash
#!/bin/bash

current_user=$(whoami)

if [ "$current_user" == "root" ]; then
    echo "You are running this script as root."
else
    echo "You are running this script as $current_user."
fi
```

Save this script as `check_user.sh`, make it executable, and run it:

```bash
chmod +x check_user.sh
./check_user.sh
```

Depending on the user running the script, it will output whether the user is `root` or another user.

#### Example 3: Combining `whoami` with Other Commands

You can combine `whoami` with other commands to make more complex commands. For example, creating a directory named after the current user:

```bash
mkdir /tmp/$(whoami)_dir
```

This will create a directory in `/tmp` with the name of the current user followed by `_dir`, such as `/tmp/ubuntu_dir`.

### Summary

The `whoami` command is straightforward but very useful, especially when you need to check or use the current user's identity in scripts and commands. It is an essential command for Linux users and administrators.
