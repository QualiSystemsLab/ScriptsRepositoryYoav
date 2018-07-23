import release_spec

mm = [{
    "StepName": "Deploy Website",
    "Version": "2.6.1.45"
}]

qq = release_spec.ReleaseSpec('aa', 'bb', '1.2.3.4', selected_packages=mm)
print qq.json
pass