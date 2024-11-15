from pcmol import Runner

model = Runner(model_id='XL', checkpoint=7, device='cuda', inference=True)
SMILES = model.targetted_generation(protein_id="P29275", batch_size=1, repeat=10)