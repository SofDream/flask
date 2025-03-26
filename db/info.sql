-- Controlla se la tabella esiste già, in caso contrario la crea
CREATE TABLE IF NOT EXISTS pianeti (
    id INTEGER PRIMARY KEY,           -- Identificativo del pianeta (0 per il Sole, 1 per il primo pianeta, ecc.)
    nome TEXT NOT NULL,
    eta INTEGER NOT NULL,             -- Età espressa in potenza di 10
    dimensioni INTEGER NOT NULL,      -- Dimensioni in km cubi, in potenza di 10
    composizione TEXT NOT NULL,       -- Composizione elementare del pianeta
    dist INTEGER NOT NULL,            -- Distanza dal Sole espressa in anni luce
    distT INTEGER NOT NULL,           -- Distanza dalla Terra espressa in anni luce
    lenY INTEGER NOT NULL             -- Durata di un anno (rivoluzione intorno al Sole) espresso in giorni
);
