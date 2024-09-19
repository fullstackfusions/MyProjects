## Common short keys

`y` - Replace the match
`n`- Skip the match
`a` - Substitutes the match and all remaining occurrences of the match
`q or Esc` - Quit substitution
`l` - Replace the match and quit
`CTRL+Y` - Scroll the screen down
`CTRL+E` - Scroll the screen up
`i` - insert mode
`v` - visual mode for CUT, COPY, PASTE
`a` - append mode
`d` - to cut the selection
`p` or `P` - to paste the selection
`:wq` - to write the changes and quit
`:q!` - to ignore the changes and quit
`dw` - to remove the word
`CTRL + R` - to redo
`u` - to undo

## Create file or edit a file

**In Mac**
`vi <file_name>`

## Insert mode:

- once you open the file press `i` for insert mode
- after which you will be able to insert anything

## Save the changes

- once you make some changes and to save them press `:wq`

## Close the file without saving any changes

- press `:q!`

## Edit the file or CUT, COPY, PASTE in different mode

**IN Visual Mode**

- once you open the file press `v` to select visual mode
- now move the cursor upto place which you want to copy
- once you selected the area
- press `y` to `COPY` and `d` to `CUT` the selcted area
- now place your cursor where you want to paste the content
- to paste the content press
- `p` to paste after cursor and `P` to paste before the cursor

## How to find and replace

`:[range]s/{pattern}/{string}/[flags]`

Let's dismantle each part and understand how it all works.

- `[range]` indicates that you can pass the range of lines. Pass % to find and replace in all lines. The range is separated by a comma. To find and replace between lines 5 to 10, pass 5,10. Use . to represent the current line and $ the last line of the file.
- `{pattern}` indicates the pattern to find the text. You can pass regex patterns here.
- `{string}` is the string to replace in the found text.
- `[flags]` indicates if you wish to pass any additional flags (for example, the flag c is passed to confirm before replacing the text). By default, this does a case-sensitive search. You can change it to do a case-insensitive search by passing a i flag.

---

- Our sample.txt file has 2 "Hello"s. Let's replace "Hello" with "Hi" at both places.
- `:%s/Hello/Hi/g`
- `%s` indicates replacing the content in the entire file
- `Hello` is the search text
- `Hi` is the text to replace
- `g` indicates making the change globally

---

Let's understand this with another example.

This time, I want to change the word "Hi" (case-insensitive search) that occurs between lines 2 and 3 and replace it with "Hello and Welcome", with a confirmation to change each occurrence.

```
Hi
Welcome to Vim Tutorial for Beginners.
Hi
```

The command to do that is:
`:2,3s/Hi/Hello and Welcome/gci`

```
Hi
Welcome to Vim Tutorial for Beginners.
Hello and Welcome
```

## How to Undo or Redo in Vim

To undo a change in Vim, press `u` in command mode. To redo, press `CTRL + R`. You can prepend a number (n) with u to undo n times. for example, `2u` will undo 2 times. To list the available undo options, type `:undolist` in command mode.

- for example I have line `Hello and Welcome`
- I have my cursor at "a" in the "Hello and Welcome" text of line. Let's remove the word "and" by typing `dw` on command mode
