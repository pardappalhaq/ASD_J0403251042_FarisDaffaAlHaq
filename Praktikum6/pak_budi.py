def get_top_k(scores, k=5):
	numbered = list(enumerate(scores, start=1))
	
	numbered.sort(key=lambda x: x[1], reverse=True)
	return numbered[:k]


def main():
	scores = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
	top5 = get_top_k(scores, 5)

	top_scores = [s for (_, s) in top5]
	print("Skor lima kandidat tertinggi (tinggi ke rendah):", top_scores)

	candidates = [i for (i, _) in top5]
	print("Kandidat yang lolos (nomor kandidat):", candidates)

if __name__ == "__main__":
	main()