import 'dart:math';

import 'package:flutter/material.dart';

class CardDisplay extends StatefulWidget {
  const CardDisplay({super.key});

  @override
  State<CardDisplay> createState() => _CardDisplayState();
}

class _CardDisplayState extends State<CardDisplay> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(5.0),
      child: Container(
        child: Center(
            child: Text(
          Random().nextInt(100).toString(),
          style: TextStyle(fontSize: 50, fontFamily: 'Poppins'),
        )),
        decoration: BoxDecoration(
            color: Color.fromARGB(255, 0, 0, 0),
            borderRadius: BorderRadius.circular(10)),
      ),
    );
  }
}
