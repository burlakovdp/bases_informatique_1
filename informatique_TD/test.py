import unittest

# Сюда вставь свою последнюю версию функции
def est_majeur(j0, m0, a0, j1, m1, a1):
    return a1 - a0 > 18 or ((a1-a0 == 18 and m1-m0 > 0) or (a1-a0 == 18 and m1-m0 == 0 and j1 -j0 >= 0))

# --- Начало набора тестов ---

class TestEstMajeur(unittest.TestCase):

    def test_personne_nettement_majeure(self):
        """Тестирует человека старше 19 лет. Должен вернуть True."""
        self.assertTrue(est_majeur(15, 5, 2004, 24, 9, 2025), "Случай: Явно совершеннолетний")

    def test_personne_nettement_mineure(self):
        """Тестирует человека младше 17 лет. Должен вернуть False."""
        self.assertFalse(est_majeur(15, 5, 2009, 24, 9, 2025), "Случай: Явно несовершеннолетний")

    def test_anniversaire_est_aujourdhui(self):
        """Тестирует человека, которому сегодня исполняется 18 лет. Должен вернуть True."""
        self.assertTrue(est_majeur(24, 9, 2007, 24, 9, 2025), "Случай: День рождения сегодня")

    def test_anniversaire_deja_passe_ce_mois_ci(self):
        """Тестирует человека, которому исполнилось 18 лет несколько дней назад. Должен вернуть True."""
        self.assertTrue(est_majeur(5, 9, 2007, 24, 9, 2025), "Случай: День рождения прошел (в этом месяце)")

    def test_anniversaire_dans_le_futur_ce_mois_ci(self):
        """Тестирует человека, которому исполнится 18 лет через несколько дней. Должен вернуть False."""
        self.assertFalse(est_majeur(28, 9, 2007, 24, 9, 2025), "Случай: День рождения скоро (в этом месяце)")
        
    def test_cas_critique_mois_futur_mais_jour_passe(self):
        """Тестирует случай, когда месяц дня рождения еще не наступил, но номер дня рождения меньше текущего. Должен вернуть False."""
        self.assertFalse(est_majeur(10, 10, 2007, 24, 9, 2025), "Случай: Будущий месяц, 'прошедший' день")

    # <-- НОВЫЙ ТЕСТ
    def test_cas_critique_mois_passe_jour_superieur(self):
        """Тестирует случай, когда месяц дня рождения прошел, но номер дня рождения больше текущего. Должен вернуть True."""
        # День рождения: 30/01/2007, Текущая дата: 24/09/2025 -> Уже 18
        self.assertTrue(est_majeur(30, 1, 2007, 24, 9, 2025), "Критический случай: Месяц прошел, но день больше")

# --- Строка для запуска тестов ---

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)