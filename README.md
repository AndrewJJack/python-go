# cmput496
* I put andrew's code into another branch called alt copy. The one in master implements timelimit using a global variable (time_limit). It also tracks who's turn it is to play at the moment with (current_player). The work we did on solver is at the bottom but it is commented out right now.<br />
* Also it might be easier to do minimax instead of negamax something like feburary 2nd slides 22-23. <br />
* I added the timer, so solve will return "unknown" if timelimit is exceded. (As a side note you call solve on a board with no legal moves it will still return "unknown")<br />
* Also changed genmove so that if it runs out of moves it just resigns, also it is now dependent on solve. If solve returns "unknown" it returns a random move, otherwise it plays the move solve gave it <br />
* **So basically all we have left to do is make the solver (I'm pretty sure lol..) We just have to put it inbetween the lines in the solve function.**<br />
* I added 4 test cases <br /> <br />

* **Don't forget to set default size of board back to 7, and turn debug mode off after we are done assignment**

