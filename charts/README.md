# Installing Helm
 
Download
```
        curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
```
Permissions
```
        chmod 700 get_helm.sh
```
Install
```
        ./get_helm.sh
```
Environment
```
        export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```
Test installation
```
        helm version
        helm ls
```

# Helm Repositories

List Helm repositories
```
helm repo list
```

Update list of Helm charts from repositories
```
helm repo update
```


# Searching Helm Charts

List all installed charts
```
helm search
```

Search for a chart
```
helm search foo
```


# Showing Installed Helm Charts

List all installed Helm charts
```
helm ls
```

List all deleted Helm charts
```
helm ls --deleted
```

List installed and deleted Helm charts
```
helm ls --all
```


# Installing/Deleting Helm charts

Inspect the variables in a chart
```
helm inspect values stable/mysql
```

Install a Helm chart
```
helm install --name foo stable/mysql
helm install --name path/to/foo
helm install --name foo bar-1.2.3.tgz
helm install --name foo https://example.com/charts/bar-1.2.3.tgz
```

Install a Helm chart and override variables
```
helm install --name foo --values config.yaml --timeout 300 --wait stable/mysql
```

Show status of Helm chart being installed
```
helm status foo
```

Delete a Helm chart
```
helm delete --purge foo
```


# Upgrading Helm Charts

Return the variables for a release
```
helm get values foo
```

Upgrade the chart or variables in a release
```
helm upgrade --values config.yaml foo stable/wordpress
```

List release numbers
```
helm history foo
```

Rollback to a previous release number
```
helm rollback foo 1
```


# Creating Helm Charts

Create a blank chart
```
helm create foo
```

Lint the chart
```
helm lint foo
```

Package the chart into foo.tgz
```
helm package foo
```

Install chart dependencies
```
helm dependency update
```

# Chart Folder Structure

```
wordpress/
  Chart.yaml          # A YAML file containing information about the chart
  LICENSE             # OPTIONAL: A plain text file containing the license for the chart
  README.md           # OPTIONAL: A human-readable README file
  requirements.yaml   # OPTIONAL: A YAML file listing dependencies for the chart
  values.yaml         # The default configuration values for this chart
  charts/             # A directory containing any charts upon which this chart depends.
  templates/          # A directory of templates that, when combined with values,
                      # will generate valid Kubernetes manifest files.
  templates/NOTES.txt # OPTIONAL: A plain text file containing short usage notes
```

