# Changelog

## 1.0.1 (2025-01-25)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/ArcadeAI/arcade-py/compare/v1.0.0...v1.0.1)

### Chores

* **internal:** codegen related update ([#92](https://github.com/ArcadeAI/arcade-py/issues/92)) ([534728b](https://github.com/ArcadeAI/arcade-py/commit/534728b5d9ac96b6e051088848bc732f05167acb))

## 1.0.0 (2025-01-24)

Full Changelog: [v0.2.2...v1.0.0](https://github.com/ArcadeAI/arcade-py/compare/v0.2.2...v1.0.0)

### Features

* **api:** api update ([#73](https://github.com/ArcadeAI/arcade-py/issues/73)) ([0f1c7ed](https://github.com/ArcadeAI/arcade-py/commit/0f1c7ed5aad99fdb3c918fbbd5513098fefa05a3))
* **api:** api update ([#75](https://github.com/ArcadeAI/arcade-py/issues/75)) ([9c9dc2d](https://github.com/ArcadeAI/arcade-py/commit/9c9dc2dc41047533f89839a0535ff13c778234ca))
* **api:** api update ([#76](https://github.com/ArcadeAI/arcade-py/issues/76)) ([641b9eb](https://github.com/ArcadeAI/arcade-py/commit/641b9eb51d3d956386f0cd55160c22d89cbcd14c))
* **api:** api update ([#82](https://github.com/ArcadeAI/arcade-py/issues/82)) ([4e66011](https://github.com/ArcadeAI/arcade-py/commit/4e6601159926eb862755e96567dc4e3726e2d97f))
* **api:** api update ([#88](https://github.com/ArcadeAI/arcade-py/issues/88)) ([a99cbe9](https://github.com/ArcadeAI/arcade-py/commit/a99cbe951cf7bcc27d86e546bdd0ad755b2246d9))
* **api:** api update ([#89](https://github.com/ArcadeAI/arcade-py/issues/89)) ([9cf3bc4](https://github.com/ArcadeAI/arcade-py/commit/9cf3bc441c103ff36c7e31a735e346078e9931bf))
* feat!: Update helper methods for client breaking changes ([#78](https://github.com/ArcadeAI/arcade-py/issues/78)) ([13cae30](https://github.com/ArcadeAI/arcade-py/commit/13cae308ab2b0c98aee51e2767cfb5fe0cb116eb))
* rc2 ([#80](https://github.com/ArcadeAI/arcade-py/issues/80)) ([bd564b9](https://github.com/ArcadeAI/arcade-py/commit/bd564b9e274df3bdcea1e2538daff9c577a0a7e3))
* Rename some class in tests ([#81](https://github.com/ArcadeAI/arcade-py/issues/81)) ([8b09459](https://github.com/ArcadeAI/arcade-py/commit/8b0945931d5b9cb4d6ae8e0fa033365b4a4617c2))


### Bug Fixes

* **client:** only call .close() when needed ([#69](https://github.com/ArcadeAI/arcade-py/issues/69)) ([b7648c0](https://github.com/ArcadeAI/arcade-py/commit/b7648c08c1c5b8bb15ffb2ca069c924506ddbfe6))
* correctly handle deserialising `cls` fields ([#72](https://github.com/ArcadeAI/arcade-py/issues/72)) ([499b981](https://github.com/ArcadeAI/arcade-py/commit/499b9816577c551d4d1a99052492aefea78a5236))
* **tests:** make test_get_platform less flaky ([#85](https://github.com/ArcadeAI/arcade-py/issues/85)) ([85da3d0](https://github.com/ArcadeAI/arcade-py/commit/85da3d0439253595655dcbf9ab4f9cb36ddda84d))


### Chores

* add missing isclass check ([#67](https://github.com/ArcadeAI/arcade-py/issues/67)) ([40bfc91](https://github.com/ArcadeAI/arcade-py/commit/40bfc912c2d9a575a157ada58b7f21f010ebb579))
* **internal:** add support for TypeAliasType ([#60](https://github.com/ArcadeAI/arcade-py/issues/60)) ([e16c393](https://github.com/ArcadeAI/arcade-py/commit/e16c393a6962d9104c066f244c883926a0bb3651))
* **internal:** avoid pytest-asyncio deprecation warning ([#86](https://github.com/ArcadeAI/arcade-py/issues/86)) ([320391e](https://github.com/ArcadeAI/arcade-py/commit/320391e2d8e195c6d4966912a7456391db8318f2))
* **internal:** bump httpx dependency ([#68](https://github.com/ArcadeAI/arcade-py/issues/68)) ([f3cab94](https://github.com/ArcadeAI/arcade-py/commit/f3cab941d45d8df5087eef3a3102eeceae84eced))
* **internal:** bump pydantic dependency ([#56](https://github.com/ArcadeAI/arcade-py/issues/56)) ([0f8197f](https://github.com/ArcadeAI/arcade-py/commit/0f8197fecb47c96cff8935f66a860ee5bd84488c))
* **internal:** bump pyright ([#59](https://github.com/ArcadeAI/arcade-py/issues/59)) ([a1a0a95](https://github.com/ArcadeAI/arcade-py/commit/a1a0a953ae35caea4ad07967caa392e9e86bd706))
* **internal:** codegen related update ([#61](https://github.com/ArcadeAI/arcade-py/issues/61)) ([87f170b](https://github.com/ArcadeAI/arcade-py/commit/87f170b0703930cf2e675c336b3b2f0f0c7eef28))
* **internal:** codegen related update ([#62](https://github.com/ArcadeAI/arcade-py/issues/62)) ([541faad](https://github.com/ArcadeAI/arcade-py/commit/541faadf245f00d7342875ec10b7cf1ecee8007b))
* **internal:** codegen related update ([#64](https://github.com/ArcadeAI/arcade-py/issues/64)) ([808aa6b](https://github.com/ArcadeAI/arcade-py/commit/808aa6b8e8b59e3bc857d6487b4e6dc601480508))
* **internal:** codegen related update ([#66](https://github.com/ArcadeAI/arcade-py/issues/66)) ([8182b3d](https://github.com/ArcadeAI/arcade-py/commit/8182b3d3106148a376534ef651ec82d128a69958))
* **internal:** codegen related update ([#71](https://github.com/ArcadeAI/arcade-py/issues/71)) ([8bf0c65](https://github.com/ArcadeAI/arcade-py/commit/8bf0c65c3d7e162716b476cdbe10969659d89085))
* **internal:** codegen related update ([#83](https://github.com/ArcadeAI/arcade-py/issues/83)) ([3d3c396](https://github.com/ArcadeAI/arcade-py/commit/3d3c396f6b97211290885afd0812f9415f8d668c))
* **internal:** codegen related update ([#87](https://github.com/ArcadeAI/arcade-py/issues/87)) ([142d2ef](https://github.com/ArcadeAI/arcade-py/commit/142d2ef3146fc7e563622a0700ff7243bcec8564))
* **internal:** fix some typos ([#65](https://github.com/ArcadeAI/arcade-py/issues/65)) ([de0fefd](https://github.com/ArcadeAI/arcade-py/commit/de0fefd92f29fd1dd7cfaf5657c12b3ddd761ac6))
* **internal:** updated imports ([#63](https://github.com/ArcadeAI/arcade-py/issues/63)) ([28ea714](https://github.com/ArcadeAI/arcade-py/commit/28ea714eede1a04b73b78a4c9447d62683acde3d))


### Documentation

* fix typos ([#70](https://github.com/ArcadeAI/arcade-py/issues/70)) ([efc448f](https://github.com/ArcadeAI/arcade-py/commit/efc448fd0f1cba242ed467e2a0480cdf1756129e))
* **raw responses:** fix duplicate `the` ([#84](https://github.com/ArcadeAI/arcade-py/issues/84)) ([19e4f04](https://github.com/ArcadeAI/arcade-py/commit/19e4f040a157de892123718adf7d027596f659e9))
* **readme:** fix http client proxies example ([#58](https://github.com/ArcadeAI/arcade-py/issues/58)) ([b8d94e8](https://github.com/ArcadeAI/arcade-py/commit/b8d94e8204e689c2957c3f72df31cedb6996c4e3))

## 0.2.2 (2024-12-04)

Full Changelog: [v0.2.1...v0.2.2](https://github.com/ArcadeAI/arcade-py/compare/v0.2.1...v0.2.2)

### Chores

* make the `Omit` type public ([#53](https://github.com/ArcadeAI/arcade-py/issues/53)) ([7512e91](https://github.com/ArcadeAI/arcade-py/commit/7512e91d0b797c51ca13e53f30029ac865075c1f))

## 0.2.1 (2024-12-03)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/ArcadeAI/arcade-py/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** version bump ([#50](https://github.com/ArcadeAI/arcade-py/issues/50)) ([d94fe99](https://github.com/ArcadeAI/arcade-py/commit/d94fe997bb6400377c4bfeec62abc68b5b233e7d))

## 0.2.0 (2024-12-03)

Full Changelog: [v0.1.2...v0.2.0](https://github.com/ArcadeAI/arcade-py/compare/v0.1.2...v0.2.0)

### Features

* **api:** api update ([#37](https://github.com/ArcadeAI/arcade-py/issues/37)) ([a545d48](https://github.com/ArcadeAI/arcade-py/commit/a545d485f3107c4888b00b83aab46274228b280e))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#48](https://github.com/ArcadeAI/arcade-py/issues/48)) ([9a0d85c](https://github.com/ArcadeAI/arcade-py/commit/9a0d85c818da37d12bc43104d90d1391b5ef674e))


### Chores

* **internal:** bump pyright ([#49](https://github.com/ArcadeAI/arcade-py/issues/49)) ([20c0925](https://github.com/ArcadeAI/arcade-py/commit/20c09258f485f11f70193dff5de8e89b04d708d6))
* **internal:** codegen related update ([#45](https://github.com/ArcadeAI/arcade-py/issues/45)) ([fb7fb4a](https://github.com/ArcadeAI/arcade-py/commit/fb7fb4ab4a45b8aa3ca42549c2624707605469b0))
* **internal:** codegen related update ([#46](https://github.com/ArcadeAI/arcade-py/issues/46)) ([6635bb1](https://github.com/ArcadeAI/arcade-py/commit/6635bb1d53d4de227d755e629236d4104d9fe85b))
* **internal:** codegen related update ([#47](https://github.com/ArcadeAI/arcade-py/issues/47)) ([61f5c17](https://github.com/ArcadeAI/arcade-py/commit/61f5c173c0792b434d2e32bb6d64be636e703355))
* **internal:** fix compat model_dump method when warnings are passed ([#43](https://github.com/ArcadeAI/arcade-py/issues/43)) ([beb8e75](https://github.com/ArcadeAI/arcade-py/commit/beb8e753294222ccbd571643ff8bf70764286744))
* rebuild project due to codegen change ([#39](https://github.com/ArcadeAI/arcade-py/issues/39)) ([e857a5a](https://github.com/ArcadeAI/arcade-py/commit/e857a5a5de9481ada4e3018399733dbc8e679518))
* rebuild project due to codegen change ([#40](https://github.com/ArcadeAI/arcade-py/issues/40)) ([123b860](https://github.com/ArcadeAI/arcade-py/commit/123b860daf2f73571dec28e4b12aab6f032e3273))
* rebuild project due to codegen change ([#41](https://github.com/ArcadeAI/arcade-py/issues/41)) ([2cf4305](https://github.com/ArcadeAI/arcade-py/commit/2cf4305f199b555c35a907bb85daf8f9f5faad5f))
* rebuild project due to codegen change ([#42](https://github.com/ArcadeAI/arcade-py/issues/42)) ([cf6455f](https://github.com/ArcadeAI/arcade-py/commit/cf6455f62312f38917c58c4f3d8dc642f92eb074))


### Documentation

* add info log level to readme ([#44](https://github.com/ArcadeAI/arcade-py/issues/44)) ([797ec03](https://github.com/ArcadeAI/arcade-py/commit/797ec036040a3afaaf65989ca0513720bbc7db36))

## 0.1.2 (2024-10-25)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/ArcadeAI/arcade-py/compare/v0.1.1...v0.1.2)

### Features

* Add auth.start and auth.wait_for_completion sugar methods ([e0b64a0](https://github.com/ArcadeAI/arcade-py/commit/e0b64a081ae91e8a560460ced6fe1e0010333987))
* Another test ([66606fe](https://github.com/ArcadeAI/arcade-py/commit/66606fe18b46808997f48c46336aaf6cbbad4165))
* Better interface for optional params ([32a92bc](https://github.com/ArcadeAI/arcade-py/commit/32a92bc92611a09078db8ed3c99e884fa8e72ba9))
* Finish tests ([7fa68e5](https://github.com/ArcadeAI/arcade-py/commit/7fa68e5bac09a5404f201d89141876d5d0de9562))
* Finish wait_for_authorization tests ([febe917](https://github.com/ArcadeAI/arcade-py/commit/febe917faa6b5ea18393cf48b21b7feeee9bfd31))
* Fix lint ([6806ee5](https://github.com/ArcadeAI/arcade-py/commit/6806ee5957042c292b80fbf7867f2bb275f8a004))
* Fix more lint ([324505c](https://github.com/ArcadeAI/arcade-py/commit/324505c86e54e7cfb95bcf6e72e881c291488c9b))
* Fix test ([07d0cf8](https://github.com/ArcadeAI/arcade-py/commit/07d0cf8eee6d1aa527fb793bb09efacadbcfa7d2))
* Fix tests ([1af1584](https://github.com/ArcadeAI/arcade-py/commit/1af15848b3fdc758818d1a7fcd692d8df68913cb))
* More tests ([caf98db](https://github.com/ArcadeAI/arcade-py/commit/caf98dbe69addd8b1edf3f68b2e06c8407d3fff6))

## 0.1.1 (2024-10-24)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/ArcadeAI/arcade-py/compare/v0.1.0...v0.1.1)

### Features

* **api:** api update ([#30](https://github.com/ArcadeAI/arcade-py/issues/30)) ([e922a94](https://github.com/ArcadeAI/arcade-py/commit/e922a9459c72d139ab4d7519abcd016d3146bd57))
* **api:** api update ([#32](https://github.com/ArcadeAI/arcade-py/issues/32)) ([78ce6cc](https://github.com/ArcadeAI/arcade-py/commit/78ce6cc0278cac884d0e15d75f681097fa5ddedc))

## 0.1.0 (2024-10-22)

Full Changelog: [v0.0.11...v0.1.0](https://github.com/ArcadeAI/arcade-py/compare/v0.0.11...v0.1.0)

### Features

* **api:** api update ([#25](https://github.com/ArcadeAI/arcade-py/issues/25)) ([c3ac0fa](https://github.com/ArcadeAI/arcade-py/commit/c3ac0fad62cf13e01f483448132d196f45f218af))
* **api:** api update ([#27](https://github.com/ArcadeAI/arcade-py/issues/27)) ([f62efbf](https://github.com/ArcadeAI/arcade-py/commit/f62efbf57628d3d9b6e2734aec1c8028e21e54b4))
* **api:** api update ([#28](https://github.com/ArcadeAI/arcade-py/issues/28)) ([5614650](https://github.com/ArcadeAI/arcade-py/commit/561465067e08077515f5e5cb361d8d09b0f7ead9))

## 0.0.11 (2024-10-15)

Full Changelog: [v0.1.0-alpha.4...v0.0.11](https://github.com/ArcadeAI/arcade-py/compare/v0.1.0-alpha.4...v0.0.11)

### Features

* **api:** api update ([#22](https://github.com/ArcadeAI/arcade-py/issues/22)) ([b4b881f](https://github.com/ArcadeAI/arcade-py/commit/b4b881fb496169501ca80a175f088780c6f4930f))

## 0.1.0-alpha.4 (2024-10-14)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/ArcadeAI/arcade-py/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** api update ([#17](https://github.com/ArcadeAI/arcade-py/issues/17)) ([c3efdc4](https://github.com/ArcadeAI/arcade-py/commit/c3efdc4cbfa3eb9e6bdd173c28ea02701ed02598))

## 0.1.0-alpha.3 (2024-10-14)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/ArcadeAI/arcade-py/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** api update ([#12](https://github.com/ArcadeAI/arcade-py/issues/12)) ([efadea8](https://github.com/ArcadeAI/arcade-py/commit/efadea87ab3842f65b9a042ad00019285199c8ba))
* **api:** api update ([#14](https://github.com/ArcadeAI/arcade-py/issues/14)) ([744e3f3](https://github.com/ArcadeAI/arcade-py/commit/744e3f3ec16f28155847fe0f195ef5b8e620859f))
* **api:** api update ([#15](https://github.com/ArcadeAI/arcade-py/issues/15)) ([4fe706f](https://github.com/ArcadeAI/arcade-py/commit/4fe706f3fb67ea7ec08e0410be1fc42f822d7f45))

## 0.1.0-alpha.2 (2024-10-14)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/ArcadeAI/arcade-py/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* remove extra fork ([f119de9](https://github.com/ArcadeAI/arcade-py/commit/f119de9e96630d4e98e7f0b9167ff950114b0b81))

## 0.1.0-alpha.1 (2024-10-13)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/ArcadeAI/arcade-py/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** api update ([0f56d0a](https://github.com/ArcadeAI/arcade-py/commit/0f56d0afea70f6d778ab4778370926b0dc1a0158))
* **api:** api update ([13f9cc9](https://github.com/ArcadeAI/arcade-py/commit/13f9cc9c8bb3f9050f64f03f61d7f079052d4ffe))
* **api:** api update ([#1](https://github.com/ArcadeAI/arcade-py/issues/1)) ([af95dc6](https://github.com/ArcadeAI/arcade-py/commit/af95dc67b673b1562dc7aacd8acf4cdfb233f2c7))
* **api:** api update ([#3](https://github.com/ArcadeAI/arcade-py/issues/3)) ([d9fc13f](https://github.com/ArcadeAI/arcade-py/commit/d9fc13f43e09e7aab1df172355f2dc514bb02ca6))
* **api:** api update ([#4](https://github.com/ArcadeAI/arcade-py/issues/4)) ([3cc79b2](https://github.com/ArcadeAI/arcade-py/commit/3cc79b24ad5c0b1bb4787d6ce6fb65bb4cf62318))
* **api:** api update ([#5](https://github.com/ArcadeAI/arcade-py/issues/5)) ([9817f3b](https://github.com/ArcadeAI/arcade-py/commit/9817f3b0ecddd33fa73c4f47bcb68fa72e703ad4))
* **api:** api update ([#6](https://github.com/ArcadeAI/arcade-py/issues/6)) ([9b88f94](https://github.com/ArcadeAI/arcade-py/commit/9b88f9494d18f3e07f8fb3f5413bcd49277472e7))
* **api:** api update ([#7](https://github.com/ArcadeAI/arcade-py/issues/7)) ([ffc6078](https://github.com/ArcadeAI/arcade-py/commit/ffc60781dfd6567ed1a64961cdc728fb87f467a4))
* **api:** api update ([#8](https://github.com/ArcadeAI/arcade-py/issues/8)) ([f151213](https://github.com/ArcadeAI/arcade-py/commit/f15121316e4a4daa4a13c8b1b3dad6af68f3aa09))
