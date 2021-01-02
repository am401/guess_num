# guess_num
This is a simple game that I started to write to improve my Python usage. The game overall is extremely simple, a random number is generated between zero and nine and you have three attempts to guess the correct number.

# Change Log
## [ 0.1 ] 2021-01-02
### Added
- Added instruction banner when playing the game to provide the range the random number will be generated in
### Change
- Moved somoe of the logic from different functions under __main__
- Changed from using `system` to `sys.exit` when exiting the program
- Changed the screen clear to directly use the `os` module
### Removed
- Removed the main() function moving the content to __main__ or guess_the_number()
