A PID (Process IDentifier) is a unique number assigned to each process in a computer system. It's used by the operating system to identify and manage processes.

A process is a running instance of a program. It includes the program code, data, and other resources needed for its execution. Processes are managed by the operating system, which allocates system resources and schedules their execution.

To find a process's PID, you can use various commands depending on your operating system. For example:

On Unix-like systems (such as Linux), you can use the ps command to list processes along with their PIDs.
On Windows, you can use Task Manager or PowerShell commands like Get-Process.
To kill a process, you typically use the kill command (on Unix-like systems) or the Stop-Process command (on Windows). You specify the PID of the process you want to terminate. Be careful when using these commands, as killing processes abruptly can lead to data loss or system instability.

A signal is a mechanism used in Unix-like operating systems to communicate with processes. Signals can be used to instruct a process to perform certain actions, such as terminating or pausing execution.

Two signals that cannot be ignored are:

SIGKILL (signal number 9): This signal forces a process to terminate immediately. It cannot be caught or ignored by the process.
SIGSTOP (signal number 19 or 17): This signal instructs a process to pause its execution. Like SIGKILL, it cannot be caught or ignored by the process.
