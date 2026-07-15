from datasets import load_dataset

print("Downloading Naija dataset...")
dataset = load_dataset("cfilt/iitbnaibn", split="train")
print(f"We have {len(dataset)} sentences!")
print("First example:", dataset[0])