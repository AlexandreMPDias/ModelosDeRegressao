import src.services.files as files

print(files.Filer.read("./data/test.txt"))
print(files.Filer.read("./data/"))

files.Filer.write("./data/yeye.json", {
	"batata": True
})