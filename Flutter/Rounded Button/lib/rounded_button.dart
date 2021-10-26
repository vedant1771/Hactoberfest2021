import 'package:flutter/material.dart';

class RoundedButton extends StatelessWidget {
  final String text;
  final Color color, textColor;
  final Function press;

  const RoundedButton(
      {Key key, this.text, this.color, this.press, this.textColor})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Material(
        color: color,
        borderRadius: BorderRadius.circular(29),
        child: InkWell(
          borderRadius: BorderRadius.circular(29),
          onTap: press,
          child: Container(
            alignment: Alignment.center,
            height: 55,
            width: size.width * .8,
            child: Text(
              text,
              style: TextStyle(color: textColor, fontWeight: FontWeight.bold),
            ),
          ),
        ));
  }
}
