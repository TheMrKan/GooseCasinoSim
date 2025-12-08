from unittest.mock import Mock, patch

from src.entities.goose import Goose, GooseGroup, WarGoose, HonkGoose
from src.entities.actor import Actor


class TestGoose:

    def setup_method(self):
        Actor.__str__ = lambda a: a.actor_id
        Actor.balance_source = {}

    def test_group_property(self):
        goose = Goose("G_0", "Name", 0.1)
        group = GooseGroup()

        goose.group = group
        assert goose.group is group
        assert goose in group

        group2 = GooseGroup()
        goose.group = group2
        assert goose.group is group2
        assert goose not in group
        assert goose in group2

    def test_use_ability_propagates(self):
        group = GooseGroup()
        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)

        goose0._ability = Mock()
        goose1._ability = Mock()

        goose0.group = group
        goose1.group = group

        goose0.use_ability(propagate=True)
        goose0._ability.assert_called_once()
        goose1._ability.assert_called_once()

    @patch('random.random')
    def test_random_run_crush(self, mock_random):
        mock_random.return_value = 0.05

        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)

        goose0.goose_source = Mock()
        goose0.goose_source.__iter__ = Mock(return_value=iter([goose0, goose1]))

        goose0.random_run()
        assert goose0.group is not None
        assert goose0.group == goose1.group

    @patch('random.random')
    def test_random_run_no_crush(self, mock_random):
        mock_random.return_value = 0.3

        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)

        goose0.goose_source = Mock()
        goose0.goose_source.__iter__ = Mock(return_value=iter([goose0, goose1]))

        goose0.random_run()
        assert goose0.group is None
        assert goose1.group is None

    @patch('random.randint')
    def test_steal(self, mock_randint):
        mock_randint.return_value = 30

        goose = Goose("G_0", "Name", 0.1)
        goose.balance_source = {}
        goose.balance = 0

        player = Mock()
        player.balance = 100
        player.actor_id = "p1"

        goose.player_source = Mock()
        goose.player_source.random_one.return_value = player

        goose.steal()

        assert player.balance == 70
        assert goose.balance == 30

    @patch('random.randint')
    def test_steal_min_balance(self, mock_randint):
        goose = Goose("G_0", "Name", 0.1)
        player = Mock()
        player.balance = 1

        goose.player_source = Mock()
        goose.player_source.random_one.return_value = player

        goose.steal()
        mock_randint.assert_not_called()

    def test_iadd_no_groups(self):
        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)

        goose0.__iadd__(goose1)
        assert goose0.group is goose1.group
        assert goose0 in goose0.group
        assert goose1 in goose0.group

    def test_iadd_one_group(self):
        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)
        grp = GooseGroup()

        goose0.group = grp
        goose0.__iadd__(goose1)

        assert goose1.group is grp
        assert goose1 in grp

    def test_iadd_two_groups(self):
        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)
        grp1 = GooseGroup()
        grp2 = GooseGroup()

        goose0.group = grp1
        goose1.group = grp2

        goose0.__iadd__(goose1)
        assert goose0.group is goose1.group

    def test_iadd_same_group(self):
        goose0 = Goose("G_0", "Name", 0.1)
        goose1 = Goose("G_1", "Name", 0.2)
        grp = GooseGroup()

        goose0.group = grp
        goose1.group = grp

        goose0.__iadd__(goose1)
        assert goose0.group is None
        assert goose1 in grp


class TestGooseGroup:
    def test_create(self):
        grp = GooseGroup()
        assert len(grp) == 0

    def test_add_remove(self):
        grp = GooseGroup()
        g = Goose("id1", "n1", 0.1)

        grp.add(g)
        assert g in grp
        assert len(grp) == 1

        grp.remove(g)
        assert g not in grp
        assert len(grp) == 0

    def test_join(self):
        grp1 = GooseGroup()
        grp2 = GooseGroup()

        g1 = Goose("id1", "n1", 0.1)
        g2 = Goose("id2", "n2", 0.2)

        g1.group = grp1
        g2.group = grp2

        grp1.join(grp2)

        assert g1.group is grp1
        assert g2.group is grp1
        assert g1 in grp1
        assert g2 in grp1

    def test_join_self(self):
        grp = GooseGroup()
        g = Goose("id1", "n1", 0.1)
        g.group = grp

        grp.join(grp)
        assert g in grp
        assert len(grp) == 1

    def test_iadd_goose(self):
        grp = GooseGroup()
        g = Goose("id1", "n1", 0.1)

        grp.__iadd__(g)
        assert g in grp

    def test_iadd_group(self):
        grp1 = GooseGroup()
        grp2 = GooseGroup()

        g1 = Goose("id1", "n1", 0.1)
        g2 = Goose("id2", "n2", 0.2)

        g1.group = grp1
        g2.group = grp2

        grp1.__iadd__(grp2)
        assert g1 in grp1
        assert g2 in grp1

    def test_isub(self):
        grp = GooseGroup()
        g = Goose("id1", "n1", 0.1)

        grp.add(g)
        grp.__isub__(g)
        assert g not in grp


class TestWarGoose:

    def test_ability(self):
        goose = WarGoose("G_0", "Name", 0.1, 20)
        player = Mock()

        goose.player_source = Mock()
        goose.player_source.random_one.return_value = player

        goose._ability()
        player.damage.assert_called_with(20)


class TestHonkGoose:

    def test_ability(self):
        goose = HonkGoose("id1", "n1", 0.1, 30)
        player = Mock()
        player.panic = 10

        goose.player_source = Mock()
        goose.player_source.random_one.return_value = player

        goose._ability()
        assert player.panic == 40
