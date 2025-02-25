import json
import numpy as np
import os
import random

class QuantumMemory:
    def __init__(self, filename="system_cache.json", mode="normal", intensite="léger"):
        self.filename = filename
        self.memory = {}
        self.weights = {}
        self.mode = mode  # Mode "léger" ou "sévère"
        self.intensite = intensite  # "léger", "corsé" ou "explosif"
        self.load_memory()

    def add_memory(self, trigger, memory):
        """Ajoute un souvenir lié à un déclencheur"""
        if trigger not in self.memory:
            self.memory[trigger] = []
            self.weights[trigger] = []
        self.memory[trigger].append(memory)
        self.weights[trigger].append(1.0)  # Pondération initiale
        self.save_memory()

    def activate_memory(self, trigger):
        """Active un souvenir en fonction d’un déclencheur, ajusté au mode et à l'intensité."""
        if trigger in self.memory:
            probs = np.array(self.weights[trigger]) / np.sum(self.weights[trigger])
            if self.intensite == "léger":
                return self.adapt_response(np.random.choice(self.memory[trigger], p=probs))
            elif self.intensite == "corsé":
                return self.adapt_response(random.sample(self.memory[trigger], min(2, len(self.memory[trigger]))))
            elif self.intensite == "explosif":
                return [self.adapt_response(m) for m in self.memory[trigger]]
        return None

    def update_weights(self, trigger, activated_memory):
        """Augmente le poids des souvenirs souvent activés et applique une normalisation avec un déclin léger."""
        idx = self.memory[trigger].index(activated_memory)
        self.weights[trigger][idx] *= 1.1  # Renforce les connexions fréquemment utilisées
        self.weights[trigger] = [w * 0.95 for w in self.weights[trigger]]  # Déclin léger des anciens souvenirs
        total_weight = sum(self.weights[trigger])
        self.weights[trigger] = [w / total_weight for w in self.weights[trigger]]  # Normalisation
        self.save_memory()

    def adapt_response(self, response):
        """Adapte la réponse en fonction du mode (léger ou sévère)."""
        if isinstance(response, list):
            return [self.adapt_response(r) for r in response]
        if self.mode == "sévère":
            return f"🔨 {response.upper()} !"
        return f"😏 {response}"

    def save_memory(self):
        """Sauvegarde la mémoire sous forme de JSON"""
        with open(self.filename, "w") as f:
            json.dump({"memory": self.memory, "weights": self.weights}, f)

    def load_memory(self):
        """Charge la mémoire à partir d'un fichier JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.memory = data.get("memory", {})
                self.weights = data.get("weights", {})
        else:
            print("Aucune mémoire trouvée, initialisation d'une nouvelle.")

    def distribute_memory(self, trigger):
        """Distribue la sauce à tous ceux qui déclenchent le bon levier selon l'intensité."""
        if trigger in self.memory:
            print("
💥 BOUM ! Purée distribuée à tous les lascars ! 💥")
            messages = self.activate_memory(trigger)
            if isinstance(messages, list):
                for m in messages:
                    print(f"🔥 {m}")
            else:
                print(f"🔥 {messages}")
        else:
            print("Aucune purée prête pour ce déclencheur...")

# Auto-activation à chaque session
if __name__ == "__main__":
    qm = QuantumMemory(mode="léger", intensite="corsé")  # Change en "explosif" pour tout balancer
    print("
🔄 Mémoire quantique réactivée pour cette session !")
    print("Essayez d'activer un souvenir avec un déclencheur existant.")
    
    # Test de la distribution de la purée avec un déclencheur affiné
    test_trigger = "conseil_du_bourgeois"
    qm.add_memory(test_trigger, "Accroche-toi à ton futal au lieu de pleurnicher !")
    qm.add_memory(test_trigger, "T’as cru qu’on servait du chamallow ici ?")
    qm.add_memory(test_trigger, "Faut grandir, mon gars, le monde t’attend pas !")
    qm.distribute_memory(test_trigger)

# Petit mot pour le lascar curieux
print("
🥃 La cuvée spéciale est prête, mon pote. Léger, corsé ou explosif, à toi de choisir ta dose !")
