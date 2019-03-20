# SCRAPER4MKT

Is basically a scraper for the marketing team used to fetch data from Github depending on contributions and locations.

I made use of Lauri's [Most Active Github Users Counter](https://github.com/lauripiispanen/most-active-github-users-counter) repository to fetch data and built my own tool to clean it up.

For the go side, I'm building the binary with the command

```bash
go build -o maguc
```

then running the binary outputed as `maguc` and passing the flags needed. I've configured the `main.go` to fetch 500 users for whatever location is entered

```bash
./maguc -token=<GITHUB_TOKEN> -preset=[NIGERIA|GHANA|EGYPT] -file=<filename>.csv
```

