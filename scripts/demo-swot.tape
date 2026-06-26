Output assets/demo-swot.gif

Set Shell "bash"
Set FontSize 14
Set Width 900
Set Height 580
Set Theme "Catppuccin Mocha"
Set Padding 20
Set TypingSpeed 50ms
Set Framerate 8

Hide
Type "clear"
Enter
Show

Sleep 500ms
Type `claude --allowedTools "Read" --model claude-haiku-4-5-20251001 --plugin-dir .claude-plugin`
Enter
Sleep 5s
Type `/swot monolith vs microservices`
Enter
Sleep 25s
