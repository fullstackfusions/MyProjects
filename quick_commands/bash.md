## Operators in bash scripts

Bash scripting supports a variety of operators for performing arithmetic, string comparison, file testing, and more. Here’s a breakdown of different categories of operators you can use in Bash scripts:

### Arithmetic Operators

These operators are used for performing basic arithmetic operations:

- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `%` : Modulus
- `**` : Exponentiation (Bash 4.0 and later)

### Relational Operators

Used in numeric comparisons:

- `-eq` : Equal to
- `-ne` : Not equal to
- `-gt` : Greater than
- `-ge` : Greater than or equal to
- `-lt` : Less than
- `-le` : Less than or equal to

### String Operators

Used for string comparisons and checks:

- `=` or `==` : Equal (for string comparison)
- `!=` : Not equal
- `<` : Less than, in ASCII alphabetical order
- `>` : Greater than, in ASCII alphabetical order
- `-z` : String is null, that is, has zero length
- `-n` : String is not null.

### Logical Operators

Used to combine conditional statements:

- `&&` : Logical AND
- `||` : Logical OR
- `!` : Logical NOT

### File Test Operators

Used to test properties of files and directories:

- `-a` : File exists (deprecated, use `-e`)
- `-e` : File exists
- `-f` : File exists and is a regular file
- `-d` : File exists and is a directory
- `-r` : File exists and is readable
- `-w` : File exists and is writable
- `-x` : File exists and is executable
- `-s` : File exists and is not empty
- `-L` : File exists and is a symbolic link
- `-S` : File exists and is a socket
- `-b` : File exists and is a block device
- `-c` : File exists and is a character device
- `-p` : File exists and is a pipe
- `-u` : File has its set-user-id bit set
- `-g` : File has its set-group-id bit set
- `-k` : File has its sticky bit set

### Assignment Operators

Used to assign values:

- `=` : Basic assignment
- `+=` : Add and assign
- `-=` : Subtract and assign
- `*=` : Multiply and assign
- `/=` : Divide and assign
- `%=` : Modulus and assign

These operators allow you to perform a wide range of tests and operations in your Bash scripts, making it possible to write complex scripts that can handle various data types and control structures.

---

## How to run in terminal

**Using Bash Editor**

- type bash
- will open bash editor
- now here you can play anything as single shot
- for example: `echo hello`
- will print hello on next line

**Using Bash File**

- first when you have to create a file with `.sh` extension
- for example in `hello.sh` we are adding `echo hello`
- in terminal we can run this file using
- `bash hello.sh`
- this will print out hello

**Without using bash before bashfile**

- so if you have noticed we have to use the `bash hello.sh`
- why this is required is because bash script always run in SHELL
- if you type echo $SHELL
- will show you something like `/bin/bash` or `/bin/zsh`
- so what we can do is we can specify this thing in any bash script
- for example in `hello.sh` we can define `#!/bin/bash` in first line along with `echo hello` in second line.
- Remember for MAC it requires `#!/bin/zsh` or your `echo $SHELL` path.
- then we can run this file without explicitly saying `bash hello.sh`, we can use `./hello.sh`
- It is possible that you will get permission error.
- for test purpose you can provide `chmod u+x <filename>`

---

## Create a multiline file for example

```bash
#!/bin/bash

echo what is your first name?
read FIRST_NAME
echo what is your last name?
read LAST_NAME

echo Hello $FIRST_NAME $LAST_NAME
```

run this file using `./<file_name.sh>`

---

## Variable Definition:

```bash
FIRST_VARIABLE = firstvalue
SECOND_VARIABLE = secondvalue
```

---

## Positional Arguments:

```bash
#!/bin/bash
echo hello $1 $2
```

- first `$0` is already reserved for shell script
- so we have started from position 1 and 2
- when we run above script
- `./file.sh Mihir Patel` will extract `Mihir` as 1st positional argument and `Patel` as 2nd positional argument

---

## Piping feature

- A bash pipe, symbolized by '|' , is a powerful tool used to pass the output of one command as input to another, with the syntax [command1] | [command2]
- Using piping the output of the first command will be passed in as input of command 2.

---

## Output redirection

- `>` to write to a file
- `>>` to append to a file
  **example**:
- `echo Hello World! > hello.txt`
- `echo Hello World! >> hello.txt`

---

## Get the word count

- `wc -w` is the commad to get the word count.
- if you want to get the word count of the file text, then type `wc -w hello.txt` will give you word count of file contenxt
- if you want to get the word count of the string, then type `wc -w <<< "give some string"` this will output `3` as the answer.

---

## EOF word

- `cat << EOF` will let you type anything line by line from terminal
- when you want to close these inputs just type `EOF` again and that will close the session

---

## if else if

#### Example-1

```bash
#!/bin/bash
if [ ${1,,} == LinuxGPT ]; then
    echo "Oh you are the boss here, how can I help you?"
else if [ ${1,,} == help ]; then
    echo "Help is on the way, please stay calm"
else
    echo "who are you? You are not allowed at this place."
fi
```

now to run this script just type: `./text.sh LinuxGPT`

#### Example-2

```bash
#!/bin/bash

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "Please provide a number as an argument."
    exit 1
fi

# Get the number from the script's argument
number=$1

# Compare the number to 10
if [ $number -gt 10 ]; then
    echo "$number is greater than 10."
elif [ $number -lt 10 ]; then
    echo "$number is less than 10."
else
    echo "$number is exactly 10."
fi
```

now to run this script just type: `./text.sh 15`

---

## case statements

#### Example-1

```bash
#!/bin/bash

echo "Enter your favorite color (red, blue, green):"
read color

case $color in
    red)
        echo "You chose red, like a rose!"
        ;;
    blue)
        echo "You chose blue, like the sky!"
        ;;
    green)
        echo "You chose green, like the grass!"
        ;;
    *)  # Default case if none of the above match
        echo "Sorry, I don't know this color."
        ;;
esac
```

To execute this script use: `./color_script.sh`

#### Example-2:

```bash
#!/bin/bash

# Script to manage services on a Linux server

echo "Welcome to the Service Manager"
echo "Please enter the service you would like to manage (e.g., nginx, apache2, mysql):"
read service
echo "Choose an action: start, stop, restart, status"
read action

case $action in
    start)
        echo "Starting $service..."
        sudo systemctl start $service
        ;;
    stop)
        echo "Stopping $service..."
        sudo systemctl stop $service
        ;;
    restart)
        echo "Restarting $service..."
        sudo systemctl restart $service
        ;;
    status)
        echo "Checking status of $service..."
        sudo systemctl status $service
        ;;
    *)
        echo "Invalid action. Please enter start, stop, restart, or status."
        ;;
esac

echo "Service management completed for $service."
```

To execute the script use: `./manage_services.sh` and follow the prompts.

---

## Arrays

```bash
#!/bin/bash

# Declare an array with initial elements
colors=('red' 'green' 'blue')   // Note: there is no comma has been used to separate the arguments

# Print all elements in the array
echo "Initial colors: ${colors[@]}"

# Add an element to the array
colors+=('yellow')

# Print all elements after adding a new one
echo "Colors after adding 'yellow': ${colors[@]}"

# Access a specific element (remember: indexing starts at 0)
echo "The second color in the list is: ${colors[1]}"

# Remove an element (remove 'green')
unset colors[1]  # This leaves a hole in the array

# Print all elements after removing 'green'
echo "Colors after removing 'green': ${colors[@]}"

# Replace an element (replace 'blue' with 'purple')
colors[2]='purple'

# Print all elements after the replacement
echo "Colors after replacing 'blue' with 'purple': ${colors[@]}"

# Loop through the array elements
echo "Looping through the array:"
for color in "${colors[@]}"; do
    echo $color
done

# Find the length of the array
echo "The array has ${#colors[@]} elements."
```

---

## For loops

#### Example-1: Bulk file processing

```bash
#!/bin/bash

# Directory containing the files
directory="/path/to/files"

# Loop over each file in the directory
for file in "$directory"/*; do
    # Check if the file is a JPEG image
    if [[ $file == *.jpg ]]; then
        # Example operation: Resize the image
        echo "Resizing $file"
        convert "$file" -resize 50% "resized_$file"
    fi
done

echo "Processing complete."
```

> **How it works**:
>
> - The script loops through each file in a specified directory.
> - It checks if the file has a .jpg extension.
> - If it does, it uses the convert command (from ImageMagick) to resize the image. Make sure ImageMagick is installed to use convert.
> - This example can be adapted for other file types or operations like data cleanup, parsing, or transformation.

#### Example-2: Monitoring Network Services status

```bash
#!/bin/bash

# Service to monitor
service="nginx"

# Delay between checks (in seconds)
delay=10

# Loop indefinitely
while true; do
    # Check if the service is active
    if systemctl is-active --quiet $service; then
        echo "$service is running."
    else
        echo "$service is not running. Attempting to restart."
        systemctl restart $service
    fi

    # Wait for the specified delay before checking again
    sleep $delay
done
```

> **How it works**:
>
> - The script continually checks whether a specified service (like nginx) is running.
> - It uses systemctl to check the service status and to restart the service if it's not running.
> - The script pauses for a specified number of seconds (delay) between checks.
> - This type of monitoring script can be very helpful for keeping critical services running on a server.

---

## Functions:

Following functions showcase different practical uses in system administration and automation, enhancing the maintainability and reusability of your scripts.

#### Example 1: Logging Function

This function helps in maintaining a log file for a script's operations, which is essential for debugging and tracking the behavior of automated tasks.

```bash
#!/bin/bash

# Function to log a message with a timestamp
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> /var/log/my_script.log
}

# Example usage of the log function
log_message "Script started."

# Perform some operations
log_message "Performing operation X."

# End of script
log_message "Script ended."
```

**How It Works:**

- `log_message` takes a single argument and appends it to a log file with a timestamp.
- The function is called at various points to log the start, during operations, and end of the script.

#### Example 2: Backup Function

This function is used to create backups of important data. It can be extended to handle different types of data and backup destinations.

```bash
#!/bin/bash

# Function to backup a directory
backup_directory() {
    local source_dir=$1
    local backup_dir=$2
    local timestamp=$(date '+%Y%m%d_%H%M%S')
    local backup_name=$(basename "$source_dir")_$timestamp.tar.gz

    tar -czf "$backup_dir/$backup_name" "$source_dir" && echo "Backup successful: $backup_name" || echo "Backup failed for $source_dir"
}

# Example usage of the backup function
backup_directory "/etc/nginx" "/backup/nginx"
```

**How It Works:**

- `backup_directory` function takes two arguments: the source directory and the backup directory.
- It creates a timestamped `.tar.gz` archive of the source directory.
- The function uses a conditional statement to print a success or failure message based on the outcome of the `tar` command.

#### Example 3: Network Check Function

This function checks the availability of a network resource (e.g., a server or API) and can be used to monitor network connectivity or service availability.

```bash
#!/bin/bash

# Function to check network connectivity to a host
check_network() {
    local host=$1
    if ping -c 1 $host &> /dev/null; then
        echo "Network check successful: $host is reachable."
    else
        echo "Network check failed: $host is not reachable."
    fi
}

# Example usage of the network check function
check_network "google.com"
```

**How It Works:**

- `check_network` function takes a hostname or IP address as an argument.
- It uses the `ping` command to test connectivity to the host.
- Outputs are redirected to null to suppress standard output and errors, focusing only on the success or failure messages.

#### Exmaple 4: Separating Local and Global parameters

```bash
#!/bin/bash
up="before"
since="function"
echo $up
echo $since
showuptime({
    local up=$(uptime -p | cut -c4-)    //defining local parameter
    local since=$(uptime -s)            //defining local parameter
    cat << EOF
---
This machine has been up for ${up}
It has been running since ${since}
---
EOF
}
showuptime  // we are calling the function here
echo $up
echo $since
```

## AWK and sed command:

Both `awk` and `sed` are powerful text-processing tools frequently used in Unix-like operating systems for scripting in data transformation, report generation, and automated edits of text files. Here are two quick examples demonstrating practical uses of each tool:

### Example 1: Using `awk` to Summarize and Report Disk Usage

Suppose you want to monitor the disk usage of a directory and generate a report based on the size of the files. You could use the `ls -l` command combined with `awk` to calculate and print the total disk usage for a specific type of file, like log files.

```bash
ls -l /var/log/*.log | awk '{sum += $5} END {print "Total disk usage for log files: " sum " bytes"}'
```

**Explanation:**

- `ls -l /var/log/*.log` lists details of log files in the `/var/log` directory.
- `awk '{sum += $5}'` adds up the sizes of the files (which appear in the fifth column of the `ls -l` output).
- `END {print "Total disk usage for log files: " sum " bytes"}` executes after processing all lines, printing the total size.

This example is particularly useful for system administrators who need to monitor disk usage in specific directories.

### Example 2: Using `sed` to Modify Configuration Files

`sed` (Stream Editor) is ideal for making automated edits to text files. For instance, changing a configuration setting in an `.ini` file without opening the file manually. Suppose you want to disable a feature by changing an `enable_feature = yes` line to `enable_feature = no` in a configuration file.

```bash
sed -i 's/enable_feature = yes/enable_feature = no/' /etc/myapp/config.ini
```

**Explanation:**

- `sed -i` edits files in-place (i.e., saves back to the original file).
- The `s/old/new/` syntax substitutes 'old' text with 'new'.
- `'s/enable_feature = yes/enable_feature = no/'` replaces `enable_feature = yes` with `enable_feature = no` in the file `/etc/myapp/config.ini`.

This command is very useful for developers and administrators when they need to programmatically alter configurations across multiple servers or during deployment.

Both of these examples demonstrate `awk` and `sed` as invaluable tools for scripting in Linux, allowing efficient manipulation of text data and files within various automation, maintenance, and monitoring tasks.
