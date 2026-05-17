# Branch Protection - Apply Manually In GitHub

Settings -> Branches -> Add branch protection rule for `main`:

- [x] Require a pull request before merging
  - [x] Require approvals: 1
  - [x] Require review from Code Owners
  - [x] Dismiss stale approvals on new commits
- [x] Require status checks to pass before merging
  - [x] Require branches to be up to date
  - Required checks:
    - `production-line / drift-guard`
    - `production-line / link-check`
- [x] Require conversation resolution before merging
- [x] Require linear history
- [x] Do not allow bypassing the above settings
- [ ] Allow force pushes  (leave OFF)
- [ ] Allow deletions     (leave OFF)

Also: Settings -> Code security
- [x] Secret scanning
- [x] Push protection
- [x] Dependabot alerts
