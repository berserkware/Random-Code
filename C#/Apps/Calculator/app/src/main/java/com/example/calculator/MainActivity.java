package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    public String Number1 = "";
    public String Number2 = "";
    public String CalculatorScreenText = "";
    public Boolean HasOperator = false;
    public String Operator = "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void OnClickOne(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "1";
        }
        else{
            Number2 += "1";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }

    public void OnClickTwo(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "2";
        }
        else{
            Number2 += "2";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickThree(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "3";
        }
        else{
            Number2 += "3";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickFour(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "4";
        }
        else{
            Number2 += "4";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickFive(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "5";
        }
        else{
            Number2 += "5";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickSix(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "6";
        }
        else{
            Number2 += "6";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickSeven(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "7";
        }
        else{
            Number2 += "7";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickEight(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "8";
        }
        else{
            Number2 += "8";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickNine(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "9";
        }
        else{
            Number2 += "9";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickZero(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += "0";
        }
        else{
            Number2 += "0";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickPlus(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false && CalculatorScreenText != ""){
            Operator = "+";
            CalculatorScreenText += "+";
            HasOperator = true;
        }
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickMinus(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false && CalculatorScreenText != ""){
            Operator = "-";
            CalculatorScreenText += "-";
            HasOperator = true;
        }
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickTimes(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false && CalculatorScreenText != ""){
            Operator = "X";
            CalculatorScreenText += "X";
            HasOperator = true;
        }
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickDivide(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false && CalculatorScreenText != ""){
            Operator = "/";
            CalculatorScreenText += "/";
            HasOperator = true;
        }
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickPoint(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        if (HasOperator == false){
            Number1 += ".";
        }
        else{
            Number2 += ".";
        }
        CalculatorScreenText = Number1 + Operator + Number2;
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickEqual(View view) {
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);

        float num1 = Float.parseFloat(Number1);
        float num2 = Float.parseFloat(Number2);

        if (Number1 != "" && Number2 != "" && HasOperator == true){

            if(Operator == "+"){
                CalculatorScreenText = String.valueOf(num1 + num2);
            }
            else if(Operator == "-"){
                CalculatorScreenText = String.valueOf(num1 - num2);
            }
            else if(Operator == "X"){
                CalculatorScreenText = String.valueOf(num1 * num2);
            }
            else if(Operator == "/"){
                CalculatorScreenText = String.valueOf(num1 / num2);
            }
        }
        Number1 = "";
        Number2 = "";
        HasOperator = false;
        Operator = "";
        CalculatorScreen.setText(CalculatorScreenText);
    }
    public void OnClickAC(View view){
        TextView CalculatorScreen = (TextView) findViewById(R.id.CalculatorScreen);
        Number1 = "";
        Number2 = "";
        CalculatorScreenText = "";
        HasOperator = false;
        Operator = "";
        CalculatorScreen.setText(CalculatorScreenText);
    }
}