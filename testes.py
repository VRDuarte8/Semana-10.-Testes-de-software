import unittest;
import numeroromano as n;


class testRomano(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.romanos = [];
    self.numeros = [1,5,2,22,9,24]
    
    self.romanos.append(n.converte('I'));
    self.romanos.append(n.converte('V'));
    self.romanos.append(n.converte('II'));
    self.romanos.append(n.converte('XXII'));
    self.romanos.append(n.converte('IX'));
    self.romanos.append(n.converte('XXIV'));

  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 
  
  def testValorRomano(self):
    print('Testar se valor em numeral corresponde ao valor em romano')
    for i in range(len(self.romanos)):
      self.assertTrue(self.romanos[i] == self.numeros [i], 'Valor incorreto ({} = {})'.format(self.romanos[i],self.numeros [i]))


if __name__ == "__main__":
  unittest.main()