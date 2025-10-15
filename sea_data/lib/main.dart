import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // Sağ üstteki debug yazısını kaldırır
      title: 'Deniz Verileri Uygulaması',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Akdeniz ve Ege Verileri")),
      body: const Center(
        child: Text(
          "Hoş geldin! 🌊",
          style: TextStyle(fontSize: 24),
        ),
      ),
    );
  }
}