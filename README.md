# pwd-shorten.py
My working directory shortener for UNIX $PS1 prompts.

## Requirements
- Python 3

## Usage
1. Add path where `pwd-shorten` is installed to your `$PATH`.
2. Add `$(pwd-shorten)` to your `$PS1` prompt.

The directory path in your prompt will be shortened:

    /very-long-directory-name/another-long-one/tacos.txt

becomes

    /ver+/ano+/tacos.txt

Home directories will be changed out as well:

    /home/jonball/example/directory

becomes

    ~/exa+/directory

## Configuration
You can override these defaults by creating a config file in `~/.config/pwd-shorten` called `config.ini` containing a top-level section titled `[settings]`.

### Config Values
The following values can be set in your config

#### `break_length`
Length at which a directory name will be shortened
- default: `5`

#### `keep_length`
How much of the original directory name to keep
- default `3`

#### `replacement`
Symbol used to indicate that a directory name has been shortened.
- default `+`

### Example Configuration

    [settings]
    break_length = 5
    keep_length  = 3
