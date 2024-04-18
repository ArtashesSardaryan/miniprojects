#!/usr/bin/python3

def get_content(fname):
	with open(fname) as f:
		return f.readlines()

def get_names(cnt):
	return [line.split()[0] for line in cnt]

def get_names_by_unique_letters(names):
	return ["".join(list(set(name.lower()))) for name in names]

def main():
	fname = "names.txt"
	cnt = get_content(fname)
	names = get_names(cnt)
	unames = get_names_by_unique_letters(names)
	unames.sort(key=len)
	print(unames[-1])


if __name__ == "__main__":
	main()
