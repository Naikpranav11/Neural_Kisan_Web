import 'package:app/Components/CardDisplay.dart';
import 'package:flutter/material.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color.fromARGB(255, 19, 19, 19),
      appBar: AppBar(
        title: Text('NeuralKissan'),
        elevation: 0,
        leadingWidth: 30,
        leading: Icon(Icons.space_dashboard_rounded),
      ),
      body: Stack(children: [
        GridView.builder(
          gridDelegate:
              SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2),
          itemBuilder: (context, index) {
            return CardDisplay();
          },
          itemCount: 5,
        )
      ]),
    );
  }
}
