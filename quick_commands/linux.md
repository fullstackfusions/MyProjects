## top commands:

- `apropos` -> Identify the Correct Command
  - for example: `apropos "copy files" `
- `;` or `&&` -> You can run multiple commands simultaneously by using `;` between them or `&&`
  - for example: `rm -v GeeksForGeeks_1.txt; mv GeeksForGeeks_2.txt gfg.txt`
  - for example: `sudo apt update && sudo apt upgrade`
- `history` -> history of the executed commands
- `sudo !!` -> use previous command in current one
- `grep` -> Grep is a useful command to search for matching patterns in a file.
- `find` -> find
- `curl` -> sending/testing http or https requests

---

## quick and short commands:

- `ls -l` -> Check permissions
- `ls -la` -> Check all files and their permissions
- `ll` -> list dorectory contents
- `chmod` -> to change the permission on file or directory
- `chown` -> change owner and group
- `pwd` -> print the working directory
- `cd` -> change directory
- `cd -` -> last working directory
- `cd ~` -> switch to user's directory
- `mkdir` -> make or create directory
- `mv` -> move file or directory
- `cp` -> copy file or directory
- `rm` -> delete files or directory
- `touch` -> create blank or empty files
- `ln` -> create symbolic link (shortcuts) to other files
- `clear` -> clear the terminal
- `cat` -> display file contents on terminal
- `echo` -> print any text that follows the command
- `less` -> display paged output in terminal
- `man` -> access manual page for all commands
- `uname` -> to get basic information of OS
- `whoami` -> get the active username
- `tar` -> command to extract and compress files
- `head` -> returns the specified numbers of lines from top
- `tail` -> returns the specified numbers of lines from bottom
- `diff` -> find difference between two files
- `cmp` -> allows you to check if two files are identical
- `comm` -> combines the functionalities of `diff` and `cmp`
- `sort` -> sort the content of the file while outputting
- `export` -> export environment variable in linux
- `zip` -> zip file in linux
- `unzip` -> unzip file in linux
- `ssh` -> secure shell command in linux
- `service` -> linux command to start and stop services
- `ps` -> display active processes
- `kill and killall` -> kill active processes by process ID or name
- `df` -> display disk file system information
- `mount` -> mount file system in linux
- `ifconfig` -> display network interfaces and ip addresses
- `traceroute` -> trace all network hops to reach the destination
- `wget` -> direct download files from internet
- `ufw` -> firewall command
- `iptables` -> base firewall for all other firewall utilities to interface with
- `apt, pacman, yum, rpm` -> package managers depending on the distribution
- `sudo` -> command to escalate privileges in Linux
- `cal` -> view a command-line calendar
- `alias` -> create custom shortcuts for your regularly used commands
- `dd` -> majorly used for creating bootable USB sticks
- `wheris` -> locate the binary, source, and manual pages for a command
- `whatis` -> find what a command is used for
- `top` -> view active processes live with their system usage
- `useradd` -> add a new user or change existing user data
- `passwd` -> create or update passwords for existing users

---

## file permissions:

- In `drwx------` d suggests that it is a directory
- In `-rwx------` - suggests that it is a file
- 3 pemission groups in linux `Owners`, `Groups`, `All Users` defined as following:

> | ---  | ---   | ---   |
> | ---- | ----- | ----- |
> | rwx  | rwx   | rwx   |
> | user | group | other |

- 3 permissions on anything `r - for read`, `w - for write`, `x - for execute`
- permission operators: `+`, `-`, `=`
- to change the permission use `chmod`
- For example: `chmod o+x xyz.txt` => we are changing `others` permission to allow execute the xyz.txt file
- For example: `chmod ugo-rwx xyz.txt`
  - The code above revokes all the read(r), write(w), and execute(x) permission from all user(u), group(g), and others(o) for the file xyz.txt which results in this.
- For example: `chmod ug=rx,o+r abc.c`
  - assigns read(r) and execute(x) permission to both user(u) and group(g) and add read permission to others for the file abc.c.

### numbered permissions:

| Octal | Binary | File Mode |
| ----- | ------ | --------- |
| 0     | 000    | ---       |
| 1     | 001    | --x       |
| 2     | 010    | -w-       |
| 3     | 011    | -wx       |
| 4     | 100    | r--       |
| 5     | 101    | r-x       |
| 6     | 110    | rw-       |
| 7     | 111    | rwx       |

- You can also define permissions with digits for all three groups as following:
- For example: `chmod 777 [file_name]` which is equal to `chmod ugo+rwx [file_name]`
- For example: `chmod 435 [file_name]` which is equal to `chmod u=r,g=wx,o=rx [file_name]`
  - Both the codes give read (code=4) user permission, write and execute (code=3) for the group and read and execute (code=5) for others.
- For example: `chmod 775 [file_name]` which is equal to `chmod ug+rwx,o=rx [file_name]`
- For example: `chmod 644 *.txt`

### recursive permissions:

- for directories and sub directories if you want to set same permissions.
- For example: `chmod -R 750 directory`

---

## curl command:

The `curl` command is a versatile tool used for transferring data to or from a server, particularly useful for interacting with web resources. It supports a variety of protocols, including HTTP, HTTPS, FTP, and more. Below are four practical examples of using `curl` commands in real project testing scenarios, particularly useful for testing APIs or web applications.

### Example 1: Simple GET Request

This command retrieves data from a specified URL. It's useful for testing API endpoints that return data based on GET requests.

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Usage**: This command is typically used to test REST API endpoints to ensure they're returning the correct data. It’s straightforward and effective for initial API responsiveness tests.

### Example 2: POST Request with JSON Payload

This command sends a POST request with JSON data to an API. This is essential for APIs that accept JSON data to create or update resources.

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title": "foo", "body": "bar", "userId": 1}'
```

**Usage**: Useful for testing the creation of resources via APIs. This ensures that the API handles new data correctly and responds with the right status codes and returns the created entity.

### Example 3: PUT Request to Update Data

This example updates data at a specific endpoint using a PUT request. It’s crucial for testing APIs that support updating existing records.

```bash
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
-H "Content-Type: application/json" \
-d '{"id": 1, "title": "updated title", "body": "updated body", "userId": 1}'
```

**Usage**: Checks if the API properly handles updates. This ensures data integrity and response accuracy after modification requests.

### Example 4: DELETE Request

This command sends a DELETE request to an API to remove a specific resource. It’s vital for APIs that allow resource deletion.

```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Usage**: Tests if the API endpoint correctly handles delete operations, ensuring that resources are not only deleted but also return appropriate responses and status codes.

### Example-5: Downloading Files

Here’s how you can use `curl` to download a file, useful for testing if file resources are accessible and served correctly.

```bash
curl -O https://example.com/somefile.zip
```

**Usage**: Ensures that files are downloadable from a given server or API and checks the integrity and availability of those files.

### different operators or arguments can be used between `curl` and `url`

These `curl` examples provide a foundational approach to testing various aspects of web APIs and servers, ensuring that each component functions correctly before going live or progressing through stages of development.

The `curl` command offers a wide array of options and arguments that enhance its functionality, making it a powerful tool for interacting with servers, APIs, and performing a variety of network operations. Below is a list of some commonly used `curl` options (or arguments) that you can use between the `curl` command and the URL you are targeting:

#### HTTP Methods

- `-X, --request <command>`: Specifies a custom request method to use when communicating with the HTTP server. Common methods include `GET`, `POST`, `PUT`, `DELETE`, etc.

#### Data Handling

- `-d, --data <data>`: Sends the specified data in a POST request to the HTTP server. Often used for submitting form data.
- `--data-urlencode <data>`: URL encodes the given data and appends it to the URL as query parameters.
- `-F, --form <name=content>`: Submits data as a multipart/form-data POST request, useful for file uploads.

#### Headers

- `-H, --header <header>`: Passes additional header(s) to the server with your request.
- `-I, --head`: Fetches the headers only, equivalent to a HEAD request.

#### Authentication

- `-u, --user <user:password>`: Passes server authentication credentials. Supports mechanisms like Basic, Digest, NTLM, and more.

#### Response Output

- `-o, --output <file>`: Writes the response output to the specified file instead of stdout.
- `-O, --remote-name`: Saves the downloaded file with the filename in the URL.

#### Security and Certificates

- `-k, --insecure`: Allows connections to SSL sites without certificates being validated.
- `--cert <certificate[:password]>`: Uses the specified client certificate file for SSL connections.

#### Connection Options

- `--connect-timeout <seconds>`: Maximum time in seconds that you allow the connection to the server to take.
- `-m, --max-time <seconds>`: Maximum time in seconds for the whole operation to take. This is useful for preventing hanging scripts.

#### Cookies

- `-b, --cookie <name=data>`: Sends cookies to the server (format as a string "name=value").
- `-c, --cookie-jar <file name>`: Saves all cookies to this file after operation (useful for sessions).

#### Proxy Support

- `-x, --proxy [protocol://]host[:port]`: Use the specified proxy.
- `--proxy-user <user:password>`: Proxy authentication credentials.

#### Verbose / Debug

- `-v, --verbose`: Makes the operation more talkative. Mostly useful for debugging a chain of proxies or the request/response headers.

#### FTP Specific

- `--ftp-ssl`: Try to use SSL/TLS for the FTP connection.
- `-P, --ftp-port <address>`: Use PORT with given address instead of PASV when connecting to an FTP server.

#### Redirection

- `-L, --location`: Follow redirects (useful when the target URL is a redirecting URL).

#### Rate Limiting

- `--limit-rate <speed>`: Limits the rate at which data is sent or received.

#### Headers and Output

- `-i, --include`: Includes the HTTP response headers in the output.

These options provide significant flexibility, allowing you to customize your `curl` commands to fit various use cases, from simple webpage downloads to complex API interactions and file transfers.

---

## find command:

- The find command in Linux is a dynamic utility designed for comprehensive file and directory searches within a hierarchical structure.
- Its adaptability allows users to search by name, size, modification time, or content, providing a flexible and potent solution.

| Command                                                                                                      | Description                                                                                                           |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| -name pattern                                                                                                | Searches for files with a specific name or pattern.                                                                   |
| -type type                                                                                                   | Specifies the type of file to search for (e.g., f for regular files, d for directories).                              |
| -size [+/-]n                                                                                                 | Searches for files based on size. `+n` finds larger files, `-n` finds smaller files. ‘n‘ measures size in characters. |
| -mtime n                                                                                                     | Finds files based on modification time. `n` represents the number of days ago.                                        |
| -exec command {} \                                                                                           | Executes a command on each file found.                                                                                |
| -print                                                                                                       | Displays the path names of files that match the specified criteria.                                                   |
| -maxdepth levels                                                                                             | Restricts the search to a specified directory depth.                                                                  |
| -mindepth levels                                                                                             | Specifies the minimum directory depth for the search.                                                                 |
| -empty                                                                                                       | Finds empty files and directories.                                                                                    |
| -delete                                                                                                      | Deletes files that match the specified criteria.                                                                      |
| -execdir command {} \|Executes a command on each file found, from the directory containing the matched file. |
| -iname pattern                                                                                               | Case-insensitive version of `-name`. Searches for files with a specific name or pattern, regardless of case.          |

### Examples:

- `find [path] [options] [expression]`
- Here, path: starting directory for the search.
- for Example: `find /path/to/search`
- options: additional settings or conditions for the search.
- for Example: `find /path/to/search -type f -name "*.txt"`
- expression: criteria for filtering and locating files.
- for Example: `find /path/to/search -type d -name "docs"`
- `find ./GFG -name *.txt` => search files with a pattern
- `find ./GFG -name sample.txt -exec rm -i {} \; ` => find and confirm file deletion
- `find ./GFG -empty` => search for empty file
- `find ./GFG -perm 664` => search files with specific permission
- `find . -type d` => display repo hierarchy
- `find ./ -type f -name "*.txt" -exec grep 'Geek'  {} \;` => search text in multiple files
- `find /path/to/search -mtime -7` => find files by when they were modified
- `find . -type f -exec grep -l "pattern" {} \;` => use grep to find files based on content
- `find /path/to/search -type f -exec grep -l "specific_text" {} \;` => same as above

### More Examples

#### Example 1: Finding Files by Name

This command searches for all files with a `.py` extension within the current directory and its subdirectories, useful for locating all Python scripts in a project.

```bash
find . -name "*.py"
```

#### Example 2: Finding and Deleting Old Files

This command finds all `.log` files in `/var/log` that are older than 30 days and deletes them, useful for cleaning up old log files to free up space.

```bash
find /var/log -name "*.log" -type f -mtime +30 -exec rm {} +
```

#### Example 3: Finding Files by Size

This command searches for files larger than 100MB within a specific directory. This is particularly useful for identifying large files that are consuming significant disk space.

```bash
find /home/user/data -type f -size +100M
```

#### Example 4: Executing Commands on Found Files

This example finds all JPEG files and converts them to PNG using ImageMagick's `convert` command, a common task in media processing projects.

```bash
find /path/to/images -type f -name "*.jpg" -exec convert {} {}.png \;
```

#### Example 5: Finding Files with Specific Permissions

This command finds all files within the `/home` directory that have '777' permissions, which could be a security risk as it means everyone has read, write, and execute permissions.

```bash
find /home -type f -perm 777
```

#### Example 6: Finding Files Modified in the Last N Days

This command finds files modified in the last 7 days within a project directory. It's useful for monitoring recently changed files or for audit purposes.

```bash
find /path/to/project -type f -mtime -7
```

#### Example 7: Finding and Archiving Files

This command finds all `.txt` files under the `/documents` directory and archives them into a tarball, useful for backup operations.

```bash
find /documents -type f -name "*.txt" -exec tar -rvf docs_backup.tar {} +
```

#### Example 8: Finding Files by Owner

This command finds all files owned by the user `username` in the `/projects` directory, useful for user-specific audits or cleanups.

```bash
find /projects -type f -user username
```

#### Example 9: Finding Empty Files and Directories

This command finds all empty files and directories within a specified directory, which can help in cleaning up unneeded empty structures.

```bash
find /path/to/check -empty
```

#### Example 10: Finding and Copying Files

This command finds all PDF files in a directory and copies them to another directory, useful for organizing files or preparing data sets.

```bash
find /path/to/reports -type f -name "*.pdf" -exec cp {} /path/to/destination/ \;
```

These examples cover a broad range of practical uses for the `find` command, demonstrating its versatility in handling files based on names, sizes, modification dates, permissions, and more. Such capabilities are essential for efficient filesystem management and automation in real-world projects.

## grep command:

- The grep command in Unix/Linux is a powerful tool used for searching and manipulating text patterns within files.
- `grep [options] pattern [files]`
- [options]: These are command-line flags that modify the behavior of grep.
- [pattern]: This is the regular expression you want to search for.
- [file]: This is the name of the file(s) you want to search within. You can specify multiple files for simultaneous searching.

**Options**

- `-c` : this prints only a count of the lines that match a pattern
- `-h` : display the matched lines, but do not display the filenames.
- `–i` : ignores, case for matching
- `-l` : displays list of a filenames only
- `-n` : display the matched lines and their line numbers
- `-v` : this prints out all the lines that do not matches the pattern
- `-e exp` : specifies expression with this option. can use multiple times
- `-f file` : takes patterns from file, one per line
- `-w` : match whole word

**Examples**:

- `grep -i "UNix" geekfile.txt` => case insensitive search
- `grep -c "unix" geekfile.txt` => displaying the count of number of matches Using grep
- `grep -l "unix" *` => display the file names that matches the pattern using grep
- `grep -l "unix" f1.txt f2.txt f3.xt f4.txt` => same as above
- `grep "os$" geekfile.txt` => matching the lines that End with a string using grep
- `grep –e "Agarwal" –e "Aggarwal" –e "Agrawal" geekfile.txt` => specifies expression with -e option
- `grep -R [Search] [directory]` => search recursively for a pattern in the directory

---

## To copy directory

- `cp -r <source directory> <destination directory>`
- for example: `cp -r ../some_folder .`
- In the example I am going one directory above the current location and copying them in current diectory

---

## To copy file

- `cp <source file> <destination dirctory>`
- for example: `cp some_foler/some.txt .`
- In example above I am copying `some.txt` from parent folder to the current directory

---

## remove file or directory

- `rm <file name>` => remove file
- `rm -r <folder/directory name>` => remove directory

---

## link command or ln command:

- `ln -s <source path> <link name>` => to create a link to another file

---

## less or cat command:

- the less command is used when the output printed by any command is larger than the screen space and needs scrolling. The less command allows the user to break down the output and scroll through it with the use of the enter or space keys.
- `cat <file name>`
- `cat /boot/grub/grub.cfg  | less`
- `cat /boot/grub/grub.cfg | less -SN` => use the `-N` flag with less to display line numbers, use the `-S` flag with less to enable line wrapping

---

## man command:

- `man ls` => will show you manual of how to use ls command

---

## uname command:

- `uname -a`
- use `uname -s` to display the kernel name.
- use `uname -n` to display the hostname.
- use `uname -r` to display the kernel release.
- use `uname -v` to display the kernel version.
- use `uname -m` to display the machine hardware name.

---

## head and tail command:

- `head <file name>`
- `tail <file_name>`

---

## diff, cmp, comm command:

- `diff <file 1> <file 2>`
- `cmp <file 1> <file 2>`
- `comm <file 1> <file2>`

---

## sort command:

- `sort <filename>` => for alphbetic order
- `sort -n file.txt` => for numerical order

---

## export command:

- `export <variable name>=<value>`

---

## ssh command:

- `ssh username@remote-server`

---

## service command:

- `service ssh status`
- `service ssh stop`
- `service ssh start`

---

## traceroute command:

- `traceroute <destination address>`

---

## wget command:

- `wget <link to file>`
- `wget -c <link to file>` => `-c` argument allows us to resume an interrupted download.

---

## package managers:

- Debian and Debian-based distros - `apt install <package name>`
- Arch and Arch-based distros - `pacman -S <package name>`
- Red Hat and Red Hat-based distros - `yum install <package name>`
- Fedora and CentOS - `yum install <package>`
