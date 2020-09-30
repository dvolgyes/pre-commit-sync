# pre-commit-sync

A simple way to keep your files in sync with a web version.
E.g. you have multiple projects and you want the same .pre-commit-config.yaml everywhere.

Then you can use a hook like this to keep your file in sync:
```
repos:
-   repo: https://github.com/dvolgyes/pre-commit-sync
    rev: "v0.2.0"
    hooks:
    -   id: pre-commit-sync
        args: ['--sync=.pre-commit-config.yaml:https://raw.githubusercontent.com/dvolgyes/pre-commit-sync/master/.pre-commit-config.yaml']
```

## How does it work?

You need to pass one or more ```--sync=FILE:URL`` or ``--sync-without-git=FILE:URL``` parameters.
The first one insits that the file must be added to git, the second allows the file not being added to git.

## An example

If you create a primary .pre-commit-config.yaml, like the above one, which refers to itself,
then in a new project it is enough to download this file once, and add it to the project.
From this moment on, the pre-commit will check if the source repository has changed or not.
E.g. you could make a github/user/companywise-precommits/.pre-commit-config.yaml, and with the
above scheme, all projects will inherit the changes.

## Issues

If you have a self-referencing hook, the hook might overwrite itself.
In order to avoid this, the hook does not modify any file which is locally changed already.

## Alternatives

Many, but i liked this solution more.
