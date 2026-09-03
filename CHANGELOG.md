# Changelog

## [1.1.3](https://github.com/tristantheb/history-content-stats/compare/v1.1.2...v1.1.3) (2026-09-03)


### Miscellaneous

* **deps:** bump actions/setup-python from 6.3.0 to 7.0.0 ([#609](https://github.com/tristantheb/history-content-stats/issues/609)) ([1a2b97c](https://github.com/tristantheb/history-content-stats/commit/1a2b97c9529f84a41d395abd1e5403b1bad3ff4b))


### CI/CD changes

* group codeql bumps ([9af1a59](https://github.com/tristantheb/history-content-stats/commit/9af1a59e5d25b46ebb318ba248a9d372bb443bbd))

## [1.1.2](https://github.com/tristantheb/history-content-stats/compare/v1.1.1...v1.1.2) (2026-06-28)


### Bug Fixes

* **sync:** parity files not updated properly ([#481](https://github.com/tristantheb/history-content-stats/issues/481)) ([a836ae7](https://github.com/tristantheb/history-content-stats/commit/a836ae792dc21126822307aafb5e5cf57e86959d))


### Miscellaneous

* **deps:** bump actions/checkout from 6.0.2 to 6.0.3 ([#398](https://github.com/tristantheb/history-content-stats/issues/398)) ([f534e51](https://github.com/tristantheb/history-content-stats/commit/f534e51f471a9a6fe1f1a1f8648126ae40ab0f0d))
* **deps:** bump actions/checkout from 6.0.3 to 7.0.0 ([#469](https://github.com/tristantheb/history-content-stats/issues/469)) ([a38a8ef](https://github.com/tristantheb/history-content-stats/commit/a38a8ef1ac6f7e0aca44a98047d1e4bd09e109cc))
* **deps:** bump actions/setup-python from 6.2.0 to 6.3.0 ([#493](https://github.com/tristantheb/history-content-stats/issues/493)) ([a821768](https://github.com/tristantheb/history-content-stats/commit/a8217686b908aba8eb9c882382a51198e3143f1d))
* **deps:** bump github/codeql-action from 4.36.0 to 4.36.1 ([#387](https://github.com/tristantheb/history-content-stats/issues/387)) ([d4bb7ff](https://github.com/tristantheb/history-content-stats/commit/d4bb7ff5de3772eacfaeb95ae7ec1328930ac0b9))
* **deps:** bump github/codeql-action from 4.36.1 to 4.36.2 ([#406](https://github.com/tristantheb/history-content-stats/issues/406)) ([ac670bd](https://github.com/tristantheb/history-content-stats/commit/ac670bd1ef1a5a5f0cc67085484f14d29e31569a))

## [1.1.1](https://github.com/tristantheb/history-content-stats/compare/v1.1.0...v1.1.1) (2026-05-30)


### Miscellaneous

* **deps:** bump github/codeql-action from 4.35.2 to 4.35.4 ([#272](https://github.com/tristantheb/history-content-stats/issues/272)) ([8a7cf33](https://github.com/tristantheb/history-content-stats/commit/8a7cf33a32d0abe3d81f2cb011eef2341c98c86c))
* **deps:** bump github/codeql-action from 4.35.4 to 4.36.0 ([#339](https://github.com/tristantheb/history-content-stats/issues/339)) ([600fa33](https://github.com/tristantheb/history-content-stats/commit/600fa3388fccb6a88292fcd07012182a8788afea))
* **deps:** bump googleapis/release-please-action from 4.4.1 to 5.0.0 ([#197](https://github.com/tristantheb/history-content-stats/issues/197)) ([0f26885](https://github.com/tristantheb/history-content-stats/commit/0f268853963d1dbef0428f3c35d9d006d3be2480))


### CI/CD changes

* poisoned sourceCommit return -1 as parity ([ea46db4](https://github.com/tristantheb/history-content-stats/commit/ea46db47cf81e6cc9527345af40d4845e2378c12))
* return better error ([e913b85](https://github.com/tristantheb/history-content-stats/commit/e913b85268dd6d94f35709dbb0cca336a6a3995b))

## [1.1.0](https://github.com/tristantheb/history-content-stats/compare/v1.0.1...v1.1.0) (2026-04-22)


### Features

* **scripts:** adding parity stats ([#175](https://github.com/tristantheb/history-content-stats/issues/175)) ([3d9c9e3](https://github.com/tristantheb/history-content-stats/commit/3d9c9e343372e8cf43febae1f8f0ccaeb634406c))


### Bug Fixes

* categories check non-strict path ([#167](https://github.com/tristantheb/history-content-stats/issues/167)) ([06bb89b](https://github.com/tristantheb/history-content-stats/commit/06bb89b57366d88088ef1e19dd16481238066e99))
* **ci:** avoid bot loop ([27c9984](https://github.com/tristantheb/history-content-stats/commit/27c99840a76a7d76f5b5ee2218347b6ff72b6504))
* crlf on stats files to lf ([4701aba](https://github.com/tristantheb/history-content-stats/commit/4701abace73778bdeb33586b23f2dcb15bbcea05))
* eol (force windows to be less stupid) ([9a557ac](https://github.com/tristantheb/history-content-stats/commit/9a557ac1e64f6b4109e6ed26bfd989e61d72a123))
* parity script update non truncated file and ignore lines. ([#179](https://github.com/tristantheb/history-content-stats/issues/179)) ([bfbab67](https://github.com/tristantheb/history-content-stats/commit/bfbab6788d9cc505f3e2b4f980979baddca77922))
* **scripts:** categories not detected properly with pathing ([#193](https://github.com/tristantheb/history-content-stats/issues/193)) ([909524d](https://github.com/tristantheb/history-content-stats/commit/909524db4a7f3ca8eaf725b88d78a59db93c9b60))
* **script:** workflow timezone isn't the same on script ([d2e93f8](https://github.com/tristantheb/history-content-stats/commit/d2e93f88140511ee7b9352061b01db71bcc02aa8))
* using same pattern for lang,locale vars ; as locale only ([#168](https://github.com/tristantheb/history-content-stats/issues/168)) ([3d824c1](https://github.com/tristantheb/history-content-stats/commit/3d824c19b4d005e558d4ab0acfffac7a048e9917))


### Miscellaneous

* update README with new file in structure ([c5539ea](https://github.com/tristantheb/history-content-stats/commit/c5539ea2237026e975e824e31999b995930e553c))


### CI/CD changes

* adding timezone on scheduled crontab ([#172](https://github.com/tristantheb/history-content-stats/issues/172)) ([3c3447c](https://github.com/tristantheb/history-content-stats/commit/3c3447c5ff101a4167c25fc57376c9bc28737340))

## [1.0.1](https://github.com/tristantheb/history-content-stats/compare/v1.0.0...v1.0.1) (2026-04-17)


### Enhancements

* **scripts:** implement lastModified date for csv ([#24](https://github.com/tristantheb/history-content-stats/issues/24)) ([acb7e89](https://github.com/tristantheb/history-content-stats/commit/acb7e8997eeff5ee6b5a28041a4d89bccdf7633b))


### Bug Fixes

* ssh method ([64267c2](https://github.com/tristantheb/history-content-stats/commit/64267c23fd965284519c1beed72edb9adc831781))
* **workflow:** error of commiter as same as reviewer ([f7e3f11](https://github.com/tristantheb/history-content-stats/commit/f7e3f113279fb6fe1dcadde720a8c1ac831dbb18))


### Miscellaneous

* **deps:** bump github/codeql-action from 4.33.0 to 4.34.0 ([#15](https://github.com/tristantheb/history-content-stats/issues/15)) ([7652d0d](https://github.com/tristantheb/history-content-stats/commit/7652d0dcb4467ccc2f531e222dafd2d8519d1eb3))
* **deps:** bump github/codeql-action from 4.34.0 to 4.34.1 ([#38](https://github.com/tristantheb/history-content-stats/issues/38)) ([d3fbae1](https://github.com/tristantheb/history-content-stats/commit/d3fbae100db4e96a7288d95b6d45da4bbfeaf76b))
* **deps:** bump github/codeql-action from 4.34.1 to 4.35.2 ([#148](https://github.com/tristantheb/history-content-stats/issues/148)) ([84b0e38](https://github.com/tristantheb/history-content-stats/commit/84b0e38715156f01ed211bd0a5a86c3f02ccee20))
* **deps:** bump googleapis/release-please-action from 4.4.0 to 4.4.1 ([#142](https://github.com/tristantheb/history-content-stats/issues/142)) ([2f38fbf](https://github.com/tristantheb/history-content-stats/commit/2f38fbf068c150d24a6e718fed34eea929151f82))
* **deps:** bump peter-evans/create-pull-request from 8.1.0 to 8.1.1 ([#137](https://github.com/tristantheb/history-content-stats/issues/137)) ([107b05c](https://github.com/tristantheb/history-content-stats/commit/107b05c8edd1ec3400707442ac9360b5dcebd3a6))


### CI/CD changes

* add ssh key for checkout ([bdf12ee](https://github.com/tristantheb/history-content-stats/commit/bdf12eee655f4532e3860f38c57a8430d1aac67d))
* fix cron time ([c7f0ddd](https://github.com/tristantheb/history-content-stats/commit/c7f0ddd947c9fb3220713e41c15df107a7d4f013))
* remove credential persistance ([fa3efe1](https://github.com/tristantheb/history-content-stats/commit/fa3efe11538be5a2f066afeeeed1375e07f158b6))
* **workflow:** silence git clone logs ([053ba09](https://github.com/tristantheb/history-content-stats/commit/053ba09eabf98ae787fbb004ecc470272db0e5cf))

## 1.0.0 (2026-03-20)


### Bug Fixes

* **ci:** auto merge for main branch ([6e23196](https://github.com/tristantheb/history-content-stats/commit/6e2319685ac847d374963cf616f681e76858f5b5))
* **ci:** pr and commit naming with hidden type ([aa29226](https://github.com/tristantheb/history-content-stats/commit/aa29226c43e127077df4ea823fbf6151b39ad93a))
* **workflow:** add missing checkout ([436f550](https://github.com/tristantheb/history-content-stats/commit/436f550877509eb3f46b6380a97559f8481ce39b))
* **workflow:** force commit signature on pr ([#6](https://github.com/tristantheb/history-content-stats/issues/6)) ([e489a91](https://github.com/tristantheb/history-content-stats/commit/e489a9112b1208547e59af2c2ca971c6b186c2f3))


### Miscellaneous

* **data:** synchronize repositories data ([#5](https://github.com/tristantheb/history-content-stats/issues/5)) ([463f251](https://github.com/tristantheb/history-content-stats/commit/463f251667ea2aa42a2161ae709a23ea9f7728ae))
* **scripts:** change script forder position ([#10](https://github.com/tristantheb/history-content-stats/issues/10)) ([2eaa34b](https://github.com/tristantheb/history-content-stats/commit/2eaa34b3f0450b93207bc332ec9afc9c01bb4947))


### CI/CD changes

* change access token ([85534c6](https://github.com/tristantheb/history-content-stats/commit/85534c628d067d667755b8dbb1bde7a945909382))
* **codeql:** adding codeql action ([#2](https://github.com/tristantheb/history-content-stats/issues/2)) ([60be04d](https://github.com/tristantheb/history-content-stats/commit/60be04dc304a5baac8e8cfe41b091355ff9fae0e))
* **workflow:** adding auto merging workflow ([#3](https://github.com/tristantheb/history-content-stats/issues/3)) ([2af7678](https://github.com/tristantheb/history-content-stats/commit/2af7678a440af1cf674804dd67dfd201c40726d4))
* **workflow:** adding logs on stats workflow ([#14](https://github.com/tristantheb/history-content-stats/issues/14)) ([ee2bc8f](https://github.com/tristantheb/history-content-stats/commit/ee2bc8fc5163ad306b3f46e78d0e54ca04ca74e3))
* **workflow:** adding repos data workflow ([#1](https://github.com/tristantheb/history-content-stats/issues/1)) ([8240e4e](https://github.com/tristantheb/history-content-stats/commit/8240e4e24f9c7497e736ab4b435c95f49a9a6eb3))
* **workflow:** adding stats generator workflow ([#7](https://github.com/tristantheb/history-content-stats/issues/7)) ([0edff11](https://github.com/tristantheb/history-content-stats/commit/0edff112d8b66572f575f77b5f88b586c62879bb))

## Changelog
