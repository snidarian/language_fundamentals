public class ColoredTerminalOutput {
    
    /*
     As per the ANSI standard all the instructions to interpret the color and positions should follow below syntax:

     Escape_character[<<code>>m <<output text>>

    Output text is the output that should be printed on the console
    Code represents the effect that should take place on console. Refer below table (Note, I'm giving only very commonly used codes here)


    Code 	Effect
    0 	    Reset all the formatting
    1 	    Bold
    3 	    Italics
    4 	    Underline
    30-37 	Each number represents one colors i.e.; 30 is for Black, 31 for Red, 32 for Green, 33 for Yellow etc.


    */

    public static void main(String[] args) {

        System.out.println("\033[31;1mHello\033[0m, \033[32;1;2mworld!\033[0m");

        System.out.println("\033[31mRed\033[32m, Green\033[33m, Yellow\033[34m, Blue\033[0m");
    }
}
