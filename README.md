# gcal
Command line Google Calendar quick-add.

## BUILD
To build, run

```shell
git clone https://github.com/AaronWebster/gcal
cd gcal
bazel build -c opt :gcal.par
```

### Update requirements.in

```shell
pipreqs --savepath=requirements.in src
```


## INSTALL
To install, copy the binary to somewhere in your path, e.g.

```shell
cp blaze-bin/gcal.par "${HOME}/bin"
```
