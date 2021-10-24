import 'package:flutter/material.dart';
import 'package:roundedbuttonflutter/rounded_button.dart';

void main(List<String> args) {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Container(
        color: Colors.white,
        height: 200,
        width: 200,
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          RoundedButton(
            color: Colors.red,
            textColor: Colors.white,
            press: () {},
            text: "I am a Rounded Button 1",
          ),
          SizedBox(
            height: 20,
          ),
          RoundedButton(
            color: Colors.deepPurple,
            textColor: Colors.white,
            press: () {},
            text: "I am a Rounded Button 2",
          ),
          SizedBox(
            height: 20,
          ),
          RoundedButton(
            color: Colors.black,
            textColor: Colors.white,
            press: () {},
            text: "I am a Rounded Button 3",
          ),
        ]),
      ),
    );
  }
}
