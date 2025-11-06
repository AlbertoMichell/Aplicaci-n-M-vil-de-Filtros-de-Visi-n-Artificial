import 'package:flutter_test/flutter_test.dart';
import 'package:filtros_vision_app/main.dart';

void main() {
  testWidgets('Prueba basica de la app', (WidgetTester tester) async {
    await tester.pumpWidget(const FiltrosVisionApp());

    expect(find.text('Filtros de Vision Artificial'), findsOneWidget);
    expect(find.text('Tomar Foto'), findsOneWidget);
    expect(find.text('Abrir Galeria'), findsOneWidget);
  });
}
