Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Exec("python main.py > logs.txt")
Set WinScriptHost = Nothing