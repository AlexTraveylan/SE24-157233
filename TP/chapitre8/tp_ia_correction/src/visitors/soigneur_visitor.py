from __future__ import annotations

from src.visitors.animal_visitor import AnimalVisitor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.animals.lion import Lion
    from src.models.animals.singe import Singe
    from src.models.animals.pingouin import Pingouin

class SoigneurVisitor(AnimalVisitor):
    def visiter_lion(self, lion: Lion) -> None:
        """Soigne et examine un lion.

        Parameters
        ----------
        lion : Lion
            L'instance du lion à soigner.

        Returns
        -------
        None
            Cette méthode ne retourne rien.

        Notes
        -----
        Augmente la santé du lion de 20 points et affiche un message
        indiquant l'examen et le niveau de santé actuel.
        """
        lion.sante += 20
        print(f"Le soigneur examine le lion {lion.nom}. Santé: {lion.sante}")
    
    def visiter_singe(self, singe: Singe) -> None:
        """Soigne et donne des vitamines à un singe.

        Parameters
        ----------
        singe : Singe
            L'instance du singe à soigner.

        Returns
        -------
        None
            Cette méthode ne retourne rien.

        Notes
        -----
        Augmente la santé du singe de 15 points et affiche un message
        indiquant l'administration de vitamines et le niveau de santé actuel.
        """
        singe.sante += 15
        print(f"Le soigneur donne des vitamines au singe {singe.nom}. Santé: {singe.sante}")
    
    def visiter_pingouin(self, pingouin: Pingouin) -> None:
        """Soigne et vérifie la température d'un pingouin.

        Parameters
        ----------
        pingouin : Pingouin
            L'instance du pingouin à soigner.

        Returns
        -------
        None
            Cette méthode ne retourne rien.

        Notes
        -----
        Augmente la santé du pingouin de 10 points et affiche un message
        indiquant la vérification de la température et le niveau de santé actuel.
        """
        pingouin.sante += 10
        print(f"Le soigneur vérifie la température du pingouin {pingouin.nom}. Santé: {pingouin.sante}") 