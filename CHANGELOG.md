# Changelog

## 1.9.0 (2025-11-04)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/ArcadeAI/arcade-py/compare/v1.8.0...v1.9.0)

### Features

* **api:** api update ([85c5f67](https://github.com/ArcadeAI/arcade-py/commit/85c5f671f829356f6b4556745785e9ecf3d86ff5))
* **api:** api update ([73a9b83](https://github.com/ArcadeAI/arcade-py/commit/73a9b83cd333bd38db8560b91764f662fa8f4e7a))
* **api:** api update ([cc7a611](https://github.com/ArcadeAI/arcade-py/commit/cc7a611b60084672f41979aea807f18249d1cb01))
* **api:** api update ([eebc9ed](https://github.com/ArcadeAI/arcade-py/commit/eebc9edf476f0838f584f6d356fdaee8d8d79c76))


### Bug Fixes

* **client:** close streams without requiring full consumption ([e5ceb83](https://github.com/ArcadeAI/arcade-py/commit/e5ceb832d91dfca38c306f69526c8a909d932f16))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([8d8e4b7](https://github.com/ArcadeAI/arcade-py/commit/8d8e4b7d707dce5a3e9869f3346cd256cd759c5c))
* do not install brew dependencies in ./scripts/bootstrap by default ([927371b](https://github.com/ArcadeAI/arcade-py/commit/927371b47365c528be87e5dce549c0363d9b7a11))
* **internal/tests:** avoid race condition with implicit client cleanup ([b14f88e](https://github.com/ArcadeAI/arcade-py/commit/b14f88efb33569f5307d9eabc4d7b6a6da9f477e))
* **internal:** detect missing future annotations with ruff ([0afbe98](https://github.com/ArcadeAI/arcade-py/commit/0afbe984f92a6323e30c8eeb50685083ad83869e))
* **internal:** grammar fix (it's -&gt; its) ([95c0ec1](https://github.com/ArcadeAI/arcade-py/commit/95c0ec14da8731bd724acb9c64973a05288c7fda))
* **internal:** update pydantic dependency ([450a852](https://github.com/ArcadeAI/arcade-py/commit/450a852ffa8000a2c7e1d4d294a925366301c3fd))
* **types:** change optional parameter type from NotGiven to Omit ([484c472](https://github.com/ArcadeAI/arcade-py/commit/484c472696a53d5b7ea9c14d9a826bc6701f0704))

## 1.8.0 (2025-09-11)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/ArcadeAI/arcade-py/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([f658a31](https://github.com/ArcadeAI/arcade-py/commit/f658a31f59d48a0b98af76f8a8c9b26c18b63c90))
* **api:** api update ([b5347f1](https://github.com/ArcadeAI/arcade-py/commit/b5347f1b9010f3fbc6021cca7815cd7b23e1024b))
* **api:** api update ([2002172](https://github.com/ArcadeAI/arcade-py/commit/2002172f8b3ae40bc4369bf2bd855d5c226f32c6))
* **client:** support file upload requests ([adee680](https://github.com/ArcadeAI/arcade-py/commit/adee6802723e2d39f46ae63d65fb8436b3407c88))
* improve future compat with pydantic v3 ([b0fee8f](https://github.com/ArcadeAI/arcade-py/commit/b0fee8f9f58da07007420ac5b741136c41672bd9))
* **types:** replace List[str] with SequenceNotStr in params ([acea6f7](https://github.com/ArcadeAI/arcade-py/commit/acea6f763810d79845f31d73e2ea79b153ca0007))


### Bug Fixes

* avoid newer type syntax ([565f29d](https://github.com/ArcadeAI/arcade-py/commit/565f29d37e13c4cb4bb7d6b6675c2a4f74a24ef0))


### Chores

* **internal:** add Sequence related utils ([bb04ab5](https://github.com/ArcadeAI/arcade-py/commit/bb04ab57e41ddc0d2053d43e8accfd4299c7803a))
* **internal:** change ci workflow machines ([3238508](https://github.com/ArcadeAI/arcade-py/commit/3238508b90610f40a34f4b3c214bb8082ac28f07))
* **internal:** codegen related update ([67c2153](https://github.com/ArcadeAI/arcade-py/commit/67c215338a0af06d69a1345d312aff24190e369f))
* **internal:** fix ruff target version ([c10bfbb](https://github.com/ArcadeAI/arcade-py/commit/c10bfbb961d2e10744e2b8fc5940cadd2a5adb74))
* **internal:** move mypy configurations to `pyproject.toml` file ([1eebbfd](https://github.com/ArcadeAI/arcade-py/commit/1eebbfd15baf996cf5f2cf50c097a7d846c3360f))
* **internal:** update comment in script ([e248479](https://github.com/ArcadeAI/arcade-py/commit/e248479421494f9f585b6a035477e95b2a04c8a1))
* **internal:** update pyright exclude list ([b322b28](https://github.com/ArcadeAI/arcade-py/commit/b322b2808fb8b419f4f895f39353e000efe51767))
* **project:** add settings file for vscode ([9611226](https://github.com/ArcadeAI/arcade-py/commit/9611226ac1d0bb9ea0e2e5cc3dbf66c392ef90af))
* update @stainless-api/prism-cli to v5.15.0 ([6fed0b8](https://github.com/ArcadeAI/arcade-py/commit/6fed0b8458e33c4abc422430069a7a22007e52c2))
* update github action ([66ec9db](https://github.com/ArcadeAI/arcade-py/commit/66ec9db0a712543f3e35554d02c2c7eb8d1f0bc1))

## 1.7.0 (2025-07-23)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/ArcadeAI/arcade-py/compare/v1.6.0...v1.7.0)

### Features

* **api:** api update ([ad08b68](https://github.com/ArcadeAI/arcade-py/commit/ad08b68a90d83b6488f7214469757354131828a3))
* **api:** api update ([ef473c5](https://github.com/ArcadeAI/arcade-py/commit/ef473c51ed732f25f731ae9e29ae5a62cf9e5928))
* **api:** api update ([a3c10fb](https://github.com/ArcadeAI/arcade-py/commit/a3c10fb94599d7e0adc0420027d35f578b5f05e0))
* **api:** api update ([9fc71d7](https://github.com/ArcadeAI/arcade-py/commit/9fc71d78c6bbf539e1de774373ed4b0fbe0c28ea))
* clean up environment call outs ([47ab416](https://github.com/ArcadeAI/arcade-py/commit/47ab416eaa76e665c7ec9d3a67b239eccc67e5e8))
* **client:** add support for aiohttp ([5066882](https://github.com/ArcadeAI/arcade-py/commit/50668821ffc127000372f06286f8eb74c02a7ab4))


### Bug Fixes

* **ci:** correct conditional ([79d08e8](https://github.com/ArcadeAI/arcade-py/commit/79d08e82eb314f465c3cd4052af53c906e4cbfd6))
* **ci:** release-doctor — report correct token name ([03cfe8a](https://github.com/ArcadeAI/arcade-py/commit/03cfe8aed6485613f5228053d313f8152f6262a3))
* **client:** don't send Content-Type header on GET requests ([6a3e11c](https://github.com/ArcadeAI/arcade-py/commit/6a3e11c209c831ae351feccda0d0f19970f1f7de))
* **parsing:** correctly handle nested discriminated unions ([7291d4f](https://github.com/ArcadeAI/arcade-py/commit/7291d4f6005e1c4ec9732ec56085031ce4b6a822))
* **parsing:** ignore empty metadata ([52e08bc](https://github.com/ArcadeAI/arcade-py/commit/52e08bcfd9aa364dbe1708799846a92ed2b3707d))
* **parsing:** parse extra field types ([034b5dc](https://github.com/ArcadeAI/arcade-py/commit/034b5dc3b14a34c445a75bfda65615b3eec6f936))


### Chores

* **ci:** change upload type ([6e96a87](https://github.com/ArcadeAI/arcade-py/commit/6e96a8738a5d6d7b4e805be9c0cbc430b6dacf90))
* **ci:** only run for pushes and fork pull requests ([f741da1](https://github.com/ArcadeAI/arcade-py/commit/f741da11f0a604bc7cf5e434578adca7a8f5e7a1))
* **internal:** bump pinned h11 dep ([d63ac0c](https://github.com/ArcadeAI/arcade-py/commit/d63ac0c1b7cfa29d44d6f69c94d28a8099f715bb))
* **package:** mark python 3.13 as supported ([7bfb29b](https://github.com/ArcadeAI/arcade-py/commit/7bfb29be939adebe113d045b2b2baa53ac1be36f))
* **readme:** fix version rendering on pypi ([c3d919a](https://github.com/ArcadeAI/arcade-py/commit/c3d919ae31ff06e4dd3f5f792dcf137c5133452d))
* **tests:** skip some failing tests on the latest python versions ([0f7a7e0](https://github.com/ArcadeAI/arcade-py/commit/0f7a7e0150f819d24f6295f98bc7102b74a4892c))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([d6a30cc](https://github.com/ArcadeAI/arcade-py/commit/d6a30cc3d80d0521cc4456d016e7a726ad1247e1))

## 1.6.0 (2025-06-18)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/ArcadeAI/arcade-py/compare/v1.5.0...v1.6.0)

### Features

* **api:** api update ([cd6f884](https://github.com/ArcadeAI/arcade-py/commit/cd6f884df03a517ad7af92d229f0178e181f52e7))
* **client:** add follow_redirects request option ([37071b8](https://github.com/ArcadeAI/arcade-py/commit/37071b84834f987c5c97bd31e42598d29079e670))


### Bug Fixes

* **client:** correctly parse binary response | stream ([30b1399](https://github.com/ArcadeAI/arcade-py/commit/30b1399ae02f8190c79b330190f834291190f76c))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([f7d916c](https://github.com/ArcadeAI/arcade-py/commit/f7d916c9c4927adc62b438b1b71eec3a242e8f3d))


### Chores

* **ci:** enable for pull requests ([181f08f](https://github.com/ArcadeAI/arcade-py/commit/181f08fa2a8bcef17a61dcefd0e4078b6f6357aa))
* **docs:** remove reference to rye shell ([bb105b1](https://github.com/ArcadeAI/arcade-py/commit/bb105b130ee4f24fe8e4a8114b464ae9789ffcd8))
* **docs:** remove unnecessary param examples ([e63f45b](https://github.com/ArcadeAI/arcade-py/commit/e63f45ba884856f91e7387ed73b87667557c8ef0))
* **internal:** update conftest.py ([6f4b908](https://github.com/ArcadeAI/arcade-py/commit/6f4b908240825138aa4f97da939fd4b8cb965bad))
* **readme:** update badges ([e0ecda6](https://github.com/ArcadeAI/arcade-py/commit/e0ecda6d97885630a77933dc7fdb57c2540c8a2d))
* **tests:** add tests for httpx client instantiation & proxies ([8328a61](https://github.com/ArcadeAI/arcade-py/commit/8328a616e0f73562720bcdeee7532887ae328999))
* **tests:** run tests in parallel ([aabdc37](https://github.com/ArcadeAI/arcade-py/commit/aabdc37b1979121dd756a6cc1dbe31145db3c9da))

## 1.5.0 (2025-06-02)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/ArcadeAI/arcade-py/compare/v1.4.0...v1.5.0)

### Features

* **api:** api update ([1e1f9ba](https://github.com/ArcadeAI/arcade-py/commit/1e1f9baf76f6bc0ba3a5099be15c3ea2c2d13c9d))
* **api:** api update ([f362ab5](https://github.com/ArcadeAI/arcade-py/commit/f362ab5666cc12ade753f440e2ed2415a814a291))
* **api:** api update ([055b14d](https://github.com/ArcadeAI/arcade-py/commit/055b14de18f70df3f17df3c7822e580189bd7754))
* **api:** api update ([439fc45](https://github.com/ArcadeAI/arcade-py/commit/439fc45322818ee4cc4ab68937e0f0f90cc7f571))


### Bug Fixes

* **docs/api:** remove references to nonexistent types ([ade9d56](https://github.com/ArcadeAI/arcade-py/commit/ade9d56256030ba632180cbd9732dea44491944d))
* **package:** support direct resource imports ([b28c43b](https://github.com/ArcadeAI/arcade-py/commit/b28c43b1c107474147a829084fe4c2918fc83506))


### Chores

* **ci:** fix installation instructions ([35ab018](https://github.com/ArcadeAI/arcade-py/commit/35ab01810788e9ed962e8ca18bc160cad13d5166))
* **ci:** upload sdks to package manager ([264c2af](https://github.com/ArcadeAI/arcade-py/commit/264c2afb311f8f0042a210fcd48bf3ae4f869b3b))
* **docs:** grammar improvements ([4039ce4](https://github.com/ArcadeAI/arcade-py/commit/4039ce4156faac6966efc62e6645328a52a3c9c3))
* **internal:** avoid errors for isinstance checks on proxies ([f6a0407](https://github.com/ArcadeAI/arcade-py/commit/f6a04072956906ba2e1f14f2938deb26fe73a93b))
* **internal:** avoid lint errors in pagination expressions ([4288f8c](https://github.com/ArcadeAI/arcade-py/commit/4288f8c7152ee984cc11db01950a12e470fd2fd3))

## 1.4.0 (2025-04-25)

Full Changelog: [v1.3.1...v1.4.0](https://github.com/ArcadeAI/arcade-py/compare/v1.3.1...v1.4.0)

### Features

* **api:** api update ([8ebf770](https://github.com/ArcadeAI/arcade-py/commit/8ebf77068b377450788bd7436bd3ed264a195805))
* **api:** api update ([db1894b](https://github.com/ArcadeAI/arcade-py/commit/db1894bccf5cfc6078133a0cbceeefc25f473532))
* **api:** api update ([fb62a65](https://github.com/ArcadeAI/arcade-py/commit/fb62a6583c4c3af75eb3789e80d79f0306a5c7ec))
* **api:** api update ([3133b01](https://github.com/ArcadeAI/arcade-py/commit/3133b01155fe75e7cfd14315ff8ab8fbabfe4ab1))
* **api:** api update ([7290dc8](https://github.com/ArcadeAI/arcade-py/commit/7290dc846a4b31d4eb5836c8d997561cacb9f2dd))
* **api:** api update ([#137](https://github.com/ArcadeAI/arcade-py/issues/137)) ([7ce1f6a](https://github.com/ArcadeAI/arcade-py/commit/7ce1f6aee46e2d8763c194a88f28428df9eb6d5f))
* **api:** api update ([#138](https://github.com/ArcadeAI/arcade-py/issues/138)) ([cb71d87](https://github.com/ArcadeAI/arcade-py/commit/cb71d87280889f8d1200be0d069a088560c1bc8b))
* **api:** api update ([#139](https://github.com/ArcadeAI/arcade-py/issues/139)) ([9a0ef5a](https://github.com/ArcadeAI/arcade-py/commit/9a0ef5a37cd20950fde494f690dd403715029243))


### Bug Fixes

* **ci:** ensure pip is always available ([#135](https://github.com/ArcadeAI/arcade-py/issues/135)) ([fd63bd1](https://github.com/ArcadeAI/arcade-py/commit/fd63bd10897027f3a2ea9e82043943213c1f897f))
* **ci:** remove publishing patch ([#136](https://github.com/ArcadeAI/arcade-py/issues/136)) ([bd4bfc8](https://github.com/ArcadeAI/arcade-py/commit/bd4bfc8d40a1a59ac65e862eb6f0e04e0184c75d))
* **perf:** optimize some hot paths ([c544b05](https://github.com/ArcadeAI/arcade-py/commit/c544b05d5afac34fe9119b791add080567f0e4cf))
* **perf:** skip traversing types for NotGiven values ([af97129](https://github.com/ArcadeAI/arcade-py/commit/af97129e7ce0dc09566e4166cbaaa2b6a2246864))
* **pydantic v1:** more robust ModelField.annotation check ([be8bb32](https://github.com/ArcadeAI/arcade-py/commit/be8bb32f9fab2a893fd6b11649c4f48b77fbd79d))
* **types:** handle more discriminated union shapes ([#134](https://github.com/ArcadeAI/arcade-py/issues/134)) ([2e8aa54](https://github.com/ArcadeAI/arcade-py/commit/2e8aa5469824223540f3c1f970662bf0ed5f62ac))


### Chores

* broadly detect json family of content-type headers ([b562715](https://github.com/ArcadeAI/arcade-py/commit/b562715e721a8aa1b53414c989fd573602e2197a))
* **ci:** add timeout thresholds for CI jobs ([467dfb2](https://github.com/ArcadeAI/arcade-py/commit/467dfb2ae0da1a048b9055630efa9a40126060dd))
* **ci:** only use depot for staging repos ([eb51e05](https://github.com/ArcadeAI/arcade-py/commit/eb51e05c0d9095ddf0cda7b97984254b03b62be1))
* **client:** minor internal fixes ([4e548b8](https://github.com/ArcadeAI/arcade-py/commit/4e548b86970ec4af361c474223255a8c847c4bff))
* **internal:** base client updates ([1a4a717](https://github.com/ArcadeAI/arcade-py/commit/1a4a717957f74170069bfff0a415ddc38e66c5ef))
* **internal:** bump pyright version ([6681c14](https://github.com/ArcadeAI/arcade-py/commit/6681c14818b989c4968408fe7432414c326d9038))
* **internal:** bump rye to 0.44.0 ([#133](https://github.com/ArcadeAI/arcade-py/issues/133)) ([0068d95](https://github.com/ArcadeAI/arcade-py/commit/0068d951be52d203c558d6a241feca26eb1f3613))
* **internal:** codegen related update ([b551ba9](https://github.com/ArcadeAI/arcade-py/commit/b551ba99820f93fdecb24663e83dff11897f8f62))
* **internal:** codegen related update ([#132](https://github.com/ArcadeAI/arcade-py/issues/132)) ([85ff426](https://github.com/ArcadeAI/arcade-py/commit/85ff426032303355d1d8c331813aaeeeaef0f69d))
* **internal:** expand CI branch coverage ([02cc295](https://github.com/ArcadeAI/arcade-py/commit/02cc2952f5b3bc36645d1da528f46ac65b681fd5))
* **internal:** fix list file params ([1f6d1f3](https://github.com/ArcadeAI/arcade-py/commit/1f6d1f33d2323d2d0dec2ccfa9e21cf0b208bdd1))
* **internal:** import reformatting ([772a87c](https://github.com/ArcadeAI/arcade-py/commit/772a87cd938e2d0f008cc54f3843ca4dad567225))
* **internal:** reduce CI branch coverage ([f6d1892](https://github.com/ArcadeAI/arcade-py/commit/f6d1892c845ee924614c174ef5bd24241b111c8c))
* **internal:** refactor retries to not use recursion ([709debf](https://github.com/ArcadeAI/arcade-py/commit/709debf17814c59c6048b996195090ee677119ed))
* **internal:** remove extra empty newlines ([#131](https://github.com/ArcadeAI/arcade-py/issues/131)) ([4a0f409](https://github.com/ArcadeAI/arcade-py/commit/4a0f4094477d25a8c213f07e33f42296864d2866))
* **internal:** remove trailing character ([#140](https://github.com/ArcadeAI/arcade-py/issues/140)) ([850838e](https://github.com/ArcadeAI/arcade-py/commit/850838edc42110c22d2c4342e4340f8322fb0e86))
* **internal:** slight transform perf improvement ([#142](https://github.com/ArcadeAI/arcade-py/issues/142)) ([af27cc2](https://github.com/ArcadeAI/arcade-py/commit/af27cc24050a658f27d49909b0596b41309c1326))
* **internal:** update models test ([ced3495](https://github.com/ArcadeAI/arcade-py/commit/ced349577a3c0c5b033ac53ebd239f333bc13fdf))
* **internal:** update pyright settings ([950f294](https://github.com/ArcadeAI/arcade-py/commit/950f294ea47c8aa6ac423b6ffd2cec37278a4b4b))


### Documentation

* revise readme docs about nested params ([#128](https://github.com/ArcadeAI/arcade-py/issues/128)) ([52f818d](https://github.com/ArcadeAI/arcade-py/commit/52f818d5bdee294add53ebc8257c6d3f48cbdd65))
* swap examples used in readme ([#141](https://github.com/ArcadeAI/arcade-py/issues/141)) ([fe028d0](https://github.com/ArcadeAI/arcade-py/commit/fe028d08aa5db60e540bca6f0635911ffcb79486))

## 1.3.1 (2025-03-11)

Full Changelog: [v1.3.0...v1.3.1](https://github.com/ArcadeAI/arcade-py/compare/v1.3.0...v1.3.1)

### Features

* **api:** api update ([#125](https://github.com/ArcadeAI/arcade-py/issues/125)) ([38ad010](https://github.com/ArcadeAI/arcade-py/commit/38ad01058bf4ffb679b5e9d7e0cad68960336a4d))

## 1.3.0 (2025-03-10)

Full Changelog: [v1.2.1...v1.3.0](https://github.com/ArcadeAI/arcade-py/compare/v1.2.1...v1.3.0)

### Features

* **api:** api update ([#116](https://github.com/ArcadeAI/arcade-py/issues/116)) ([398641f](https://github.com/ArcadeAI/arcade-py/commit/398641f2805b34f760ede51ac16e9eb3bebf7a23))
* **api:** api update ([#117](https://github.com/ArcadeAI/arcade-py/issues/117)) ([6e333f1](https://github.com/ArcadeAI/arcade-py/commit/6e333f122a4718ac9e909258774b509ef2eea1f3))
* **api:** api update ([#118](https://github.com/ArcadeAI/arcade-py/issues/118)) ([83cf396](https://github.com/ArcadeAI/arcade-py/commit/83cf3964ed5f25447e63a2e3d02e48bf5cb6ff9f))
* **api:** api update ([#119](https://github.com/ArcadeAI/arcade-py/issues/119)) ([e618af4](https://github.com/ArcadeAI/arcade-py/commit/e618af4a69d6a05dcf7622d722b9440e839b86f4))
* **api:** api update ([#123](https://github.com/ArcadeAI/arcade-py/issues/123)) ([c145e1e](https://github.com/ArcadeAI/arcade-py/commit/c145e1e78a32f83a6a5bc4bb849cc7c716632972))


### Chores

* **docs:** update client docstring ([#121](https://github.com/ArcadeAI/arcade-py/issues/121)) ([a30a866](https://github.com/ArcadeAI/arcade-py/commit/a30a866d1bd1148670cba44558abf07c7a2ac70b))
* **internal:** properly set __pydantic_private__ ([#114](https://github.com/ArcadeAI/arcade-py/issues/114)) ([558c1bb](https://github.com/ArcadeAI/arcade-py/commit/558c1bb39b9d0aa30f267217642f1a2da6a6d092))
* **internal:** remove unused http client options forwarding ([#122](https://github.com/ArcadeAI/arcade-py/issues/122)) ([6f0d183](https://github.com/ArcadeAI/arcade-py/commit/6f0d183deaf26b9176ba125342c40eb19a7783ae))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#120](https://github.com/ArcadeAI/arcade-py/issues/120)) ([df64b6f](https://github.com/ArcadeAI/arcade-py/commit/df64b6f7d7c6c4c76484dec5890f997701bd6056))

## 1.2.1 (2025-02-22)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/ArcadeAI/arcade-py/compare/v1.2.0...v1.2.1)

### Chores

* **internal:** fix devcontainers setup ([#111](https://github.com/ArcadeAI/arcade-py/issues/111)) ([b8d223b](https://github.com/ArcadeAI/arcade-py/commit/b8d223b1c79a7f403bdc7334dc27835e11cacf83))

## 1.2.0 (2025-02-21)

Full Changelog: [v1.1.1...v1.2.0](https://github.com/ArcadeAI/arcade-py/compare/v1.1.1...v1.2.0)

### Features

* **api:** api update ([#105](https://github.com/ArcadeAI/arcade-py/issues/105)) ([7ed533f](https://github.com/ArcadeAI/arcade-py/commit/7ed533fca689340285fe5b194efd5b0f233e3bd4))
* **api:** api update ([#108](https://github.com/ArcadeAI/arcade-py/issues/108)) ([ba6ddc9](https://github.com/ArcadeAI/arcade-py/commit/ba6ddc9d5d7d94fbf7764aff94b5fd8a6c28e7fa))
* **client:** allow passing `NotGiven` for body ([#109](https://github.com/ArcadeAI/arcade-py/issues/109)) ([920d114](https://github.com/ArcadeAI/arcade-py/commit/920d114c56a7d31ef0914b6bff37d4928240622a))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#107](https://github.com/ArcadeAI/arcade-py/issues/107)) ([3252ac3](https://github.com/ArcadeAI/arcade-py/commit/3252ac3b2af698fd007f045e45097e858842b575))
* **client:** mark some request bodies as optional ([920d114](https://github.com/ArcadeAI/arcade-py/commit/920d114c56a7d31ef0914b6bff37d4928240622a))

## 1.1.1 (2025-02-13)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/ArcadeAI/arcade-py/compare/v1.1.0...v1.1.1)

### Chores

* **internal:** update client tests ([#102](https://github.com/ArcadeAI/arcade-py/issues/102)) ([0607580](https://github.com/ArcadeAI/arcade-py/commit/06075801fe24e88ee7751c064ae00d8a0d597bdf))

## 1.1.0 (2025-02-07)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/ArcadeAI/arcade-py/compare/v1.0.1...v1.1.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#98](https://github.com/ArcadeAI/arcade-py/issues/98)) ([ed2a2f9](https://github.com/ArcadeAI/arcade-py/commit/ed2a2f91ed9b0d0f97bf70ad63006b59ff0a7e96))


### Chores

* **internal:** bummp ruff dependency ([#97](https://github.com/ArcadeAI/arcade-py/issues/97)) ([354784c](https://github.com/ArcadeAI/arcade-py/commit/354784ce85e1327bfde56746da97cc2016690a61))
* **internal:** change default timeout to an int ([#95](https://github.com/ArcadeAI/arcade-py/issues/95)) ([bcac267](https://github.com/ArcadeAI/arcade-py/commit/bcac26785cf90888478adb3455b2e667d442c135))
* **internal:** fix type traversing dictionary params ([#99](https://github.com/ArcadeAI/arcade-py/issues/99)) ([8d4ccf0](https://github.com/ArcadeAI/arcade-py/commit/8d4ccf0f26850f9cbb2e76c0126712f8a87567f8))
* **internal:** minor type handling changes ([#100](https://github.com/ArcadeAI/arcade-py/issues/100)) ([3adf96e](https://github.com/ArcadeAI/arcade-py/commit/3adf96e565dcf2c62ed0490fb92833a09dd2a1f8))

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
