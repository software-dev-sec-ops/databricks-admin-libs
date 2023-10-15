# databricks-admin-libs

Sample Repo to perform SCA on open source python packages

## Local Setup

### Pre-requisities
* Install Python        3.11.5
* Install virtualenv    20.23.0

```
# create virtualenv and activate environment
virtualenv myenv -p $(which python3) \
&& source myenv/bin/activate

# install required software
pip install -no-cache-dir "<library>==<version>"
```
> NOTE: Install specific versions of library

## Databricks Cluster Library Installation

* Libraries installed on the cluster are available to every notebook attached to the cluster.
* Libraries can be installed on the cluster in several ways. Read [here](https://docs.databricks.com/en/libraries/cluster-libraries.html) to learn more
> Recommendation - Use databricks cluster scoped init (bash) scripts to install packages
* Use `/databricks/python/bin/pip` to install packages on the cluster
* `init` scripts can be stored in `workspaces or unity catalog or cloud object storage (recommendation)`
* For `init` scripts stored with object storage 
    ```
    abfss://container-name@storage-account-name.dfs.core.windows.net/path/to/init-script
    ```
* Init script start and finish events are captured in cluster event logs.
* the init script logs are written to `/<cluster-log-path>/<cluster-id>/init_scripts`

## Why not manually install packages via UI?

* No Version control
* Installed software is not verified for security vulnerabilities
* Automation reduces manual intervention & installation across each cluster


## Databricks CLI

1.  Install CLI
```
brew tap databricks/tap
brew install databricks
```

2. Configure to authenticate CLI with your workspace

```
databricks configure --host <WORKSPACE_URL> --token <PERSONAL_ACCESS_TOKEN>
```



