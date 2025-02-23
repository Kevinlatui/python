import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const characters = [
  { name: "Hero", rarity: "Common" },
  { name: "Warrior", rarity: "Common" },
  { name: "Mage", rarity: "Rare" },
  { name: "Assassin", rarity: "Rare" },
  { name: "Dragon Knight", rarity: "Epic" },
  { name: "Phoenix", rarity: "Epic" },
  { name: "Celestial Guardian", rarity: "Legendary" },
];

const rarityColors = {
  Common: "text-gray-500",
  Rare: "text-blue-500",
  Epic: "text-purple-500",
  Legendary: "text-yellow-500",
};

const getRandomCharacter = () => {
  const rand = Math.random();
  if (rand < 0.5) return characters.filter(c => c.rarity === "Common")[Math.floor(Math.random() * 2)];
  if (rand < 0.8) return characters.filter(c => c.rarity === "Rare")[Math.floor(Math.random() * 2)];
  if (rand < 0.95) return characters.filter(c => c.rarity === "Epic")[Math.floor(Math.random() * 2)];
  return characters.find(c => c.rarity === "Legendary");
};

export default function GachaApp() {
  const [history, setHistory] = useState([]);
  const [currency, setCurrency] = useState(100);

  const pullCharacter = () => {
    if (currency < 10) return;
    const newCharacter = getRandomCharacter();
    setHistory([newCharacter, ...history]);
    setCurrency(currency - 10);
  };

  return (
    <div className="flex flex-col items-center p-5">
      <h1 className="text-2xl font-bold">Gacha Game</h1>
      <p className="mb-4">Currency: {currency}</p>
      <Button onClick={pullCharacter} disabled={currency < 10}>
        Pull (10 Coins)
      </Button>
      <div className="mt-5 w-full max-w-md">
        {history.map((char, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-2"
          >
            <Card>
              <CardContent className={`p-4 ${rarityColors[char.rarity]}`}>
                {char.name} - {char.rarity}
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
