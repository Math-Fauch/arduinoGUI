#include <LiquidCrystal.h>
// C++ code
//
const int LCD_RS = 12;
const int LCD_EN = 11;
const int LCD_D4 = 5;
const int LCD_D5 = 4;
const int LCD_D6 = 3;
const int LCD_D7 = 2;

// On initialise l’ecran LCD avec les bonnes PINS
LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);
char exempleChar = 'C';
int exempleNbr = 8;

void setup()
{
  lcd.begin(16, 2);
}

void loop()
{
  lcd.setCursor(0, 0);
  lcd.print("Yo le LCD"); // exemple de texte
  lcd.setCursor(13, 0); // exemple de choix d'endroit de texte
  lcd.print(exempleNbr); // exemple de numéro
  lcd.print((char)223); // exemple de charactère funky
  lcd.print(exempleChar); // exemple de variable
  lcd.setCursor(0, 1); // exemple de texte sur deuxième ligne
  lcd.print("fonctionne!!1!");
  delay(100);
}