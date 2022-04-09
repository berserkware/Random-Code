package com.example.tictactoe;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    public boolean[] isPlayed = {false, false, false, false, false, false, false, false, false};
    public String[] TicTacToeBoard = { "", "", "", "", "", "", "", "", "" };
    public boolean XWon = false;
    public boolean OWon = false;
    public boolean Turn = false;
    //if it is false it is X turn
    //if it is true it is O turn
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }
    public void Check(){
        if(!XWon && !OWon){
            TextView tv = (TextView) findViewById(R.id.textView);
            if(TicTacToeBoard[0] == "X" && TicTacToeBoard[1] == "X" && TicTacToeBoard[2] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[0] == "O" && TicTacToeBoard[1] == "O" && TicTacToeBoard[2] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[3] == "X" && TicTacToeBoard[4] == "X" && TicTacToeBoard[5] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[3] == "O" && TicTacToeBoard[4] == "O" && TicTacToeBoard[5] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[6] == "X" && TicTacToeBoard[7] == "X" && TicTacToeBoard[8] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[6] == "O" && TicTacToeBoard[7] == "O" && TicTacToeBoard[8] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[0] == "X" && TicTacToeBoard[3] == "X" && TicTacToeBoard[6] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[0] == "O" && TicTacToeBoard[3] == "O" && TicTacToeBoard[6] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[1] == "X" && TicTacToeBoard[4] == "X" && TicTacToeBoard[7] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[1] == "O" && TicTacToeBoard[4] == "O" && TicTacToeBoard[7] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[2] == "X" && TicTacToeBoard[5] == "X" && TicTacToeBoard[8] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[2] == "O" && TicTacToeBoard[5] == "O" && TicTacToeBoard[8] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[0] == "X" && TicTacToeBoard[4] == "X" && TicTacToeBoard[8] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[0] == "O" && TicTacToeBoard[4] == "O" && TicTacToeBoard[8] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(TicTacToeBoard[2] == "X" && TicTacToeBoard[4] == "X" && TicTacToeBoard[6] == "X"){
                tv.setText("X Wins!");
                XWon = true;
            }
            else if(TicTacToeBoard[2] == "O" && TicTacToeBoard[4] == "O" && TicTacToeBoard[6] == "O"){
                tv.setText("O Wins!");
                OWon = true;
            }

            if(isPlayed[0] = true && isPlayed[1] == true && isPlayed[2] == true && isPlayed[3] == true && isPlayed[4] == true && isPlayed[5] == true && isPlayed[6] == true && isPlayed[7] == true && isPlayed[8] == true){
                tv.setText("Tie!");
            }
        }
    }

    public void NextTurn(){
        if (Turn){
            TextView turnText = (TextView) findViewById(R.id.textView2);
            turnText.setText("X Turn");
            Turn = !Turn;
        }
        else if (!Turn){
            TextView turnText = (TextView) findViewById(R.id.textView2);
            turnText.setText("O Turn");
            Turn = !Turn;
        }
    }

    public void OnClickOne(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button);

            if (isPlayed[0] == false) {
                if (Turn) {
                    isPlayed[0] = true;
                    TicTacToeBoard[0] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[0] = true;
                    TicTacToeBoard[0] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickTwo(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button2);
            if (isPlayed[1] == false) {
                if (Turn) {
                    isPlayed[1] = true;
                    TicTacToeBoard[1] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[1] = true;
                    TicTacToeBoard[1] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickThree(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button3);
            if (isPlayed[2] == false) {
                if (Turn) {
                    isPlayed[2] = true;
                    TicTacToeBoard[2] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[2] = true;
                    TicTacToeBoard[2] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickFour(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button4);
            if (isPlayed[3] == false) {
                if (Turn) {
                    isPlayed[3] = true;
                    TicTacToeBoard[3] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[3] = true;
                    TicTacToeBoard[3] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickFive(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button5);
            if (isPlayed[4] == false) {
                if (Turn) {
                    isPlayed[4] = true;
                    TicTacToeBoard[4] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[4] = true;
                    TicTacToeBoard[4] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickSix(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button6);
            if (isPlayed[5] == false) {
                if (Turn) {
                    isPlayed[5] = true;
                    TicTacToeBoard[5] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[5] = true;
                    TicTacToeBoard[5] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickSeven(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button7);
            if (isPlayed[6] == false) {
                if (Turn) {
                    isPlayed[6] = true;
                    TicTacToeBoard[6] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[6] = true;
                    TicTacToeBoard[6] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickEight(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button8);
            if (isPlayed[7] == false) {
                if (Turn) {
                    isPlayed[7] = true;
                    TicTacToeBoard[7] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[7] = true;
                    TicTacToeBoard[7] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickNine(View view){
        if(!XWon && !OWon) {
            Button button = (Button) findViewById(R.id.button9);
            if (isPlayed[8] == false) {
                if (Turn) {
                    isPlayed[8] = true;
                    TicTacToeBoard[8] = "O";
                    button.setText("O");

                } else if (!Turn) {
                    isPlayed[8] = true;
                    TicTacToeBoard[8] = "X";
                    button.setText("X");
                }
                Check();
                NextTurn();
            }
        }
    }
    public void OnClickRestart(View view){
        //this resets everything
        Button button = (Button)findViewById(R.id.button);
        Button button2 = (Button)findViewById(R.id.button2);
        Button button3 = (Button)findViewById(R.id.button3);
        Button button4 = (Button)findViewById(R.id.button4);
        Button button5 = (Button)findViewById(R.id.button5);
        Button button6 = (Button)findViewById(R.id.button6);
        Button button7 = (Button)findViewById(R.id.button7);
        Button button8 = (Button)findViewById(R.id.button8);
        Button button9 = (Button)findViewById(R.id.button9);

        button.setText("1");
        button2.setText("2");
        button3.setText("3");
        button4.setText("4");
        button5.setText("5");
        button6.setText("6");
        button7.setText("7");
        button8.setText("8");
        button9.setText("9");

        TextView turnText = (TextView) findViewById(R.id.textView2);
        turnText.setText("X Turn");
        TextView tv = (TextView) findViewById(R.id.textView);
        tv.setText("");

        isPlayed[0] = false;
        isPlayed[1] = false;
        isPlayed[2] = false;
        isPlayed[3] = false;
        isPlayed[4] = false;
        isPlayed[5] = false;
        isPlayed[6] = false;
        isPlayed[7] = false;
        isPlayed[8] = false;
        TicTacToeBoard[0] = "";
        TicTacToeBoard[1] = "";
        TicTacToeBoard[2] = "";
        TicTacToeBoard[3] = "";
        TicTacToeBoard[4] = "";
        TicTacToeBoard[5] = "";
        TicTacToeBoard[6] = "";
        TicTacToeBoard[7] = "";
        TicTacToeBoard[8] = "";
        XWon = false;
        OWon = false;
    }


}