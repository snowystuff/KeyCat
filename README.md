# KeyCat
Command line tool for a simple key management database!
Can be used on webservers using PHP, offline, etc.

## How to use
Run KeyCat from command line (cmd, shell, Terminal) using `keycat command -args`

## Commands
> \[Required argument] \(Optional argument)

### Activation
Generate `gen (type) (count)`: Generates amount of keys of a specific type (default: "default")

Activate `act [key] [value]`: Activates key and links it with specified value

Verify `ver [key] [value]`: Returns true if the value matches the keys linked value

Deactivate `dac [key]`: Manually deactivates key

### Deletion
Delete `del [key]`: Deletes specified key from database

Clear (Unused/Deactivated) `cl/clu/cld (type)`: Clears all specified keys from database

### Type management
Type `tp add/del [type name] (add)[time]`: Adds or deletes type with specified length before auto-deactivation
