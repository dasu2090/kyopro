1. ルートテーブル (Route Table)

- 概要: VPC内のサブネットに関連づけて使用し、サブネットから外部への通信の行き先を決定するルールを定義。
- ルールの優先順位: 最も具体的なルールが優先される（例: 10.0.0.0/21が最優先で、次に0.0.0.0/0）。
- 例:
- 10.0.0.0/21: ターゲット「local」(VPC内のローカルネットワーク)
- 0.0.0.0/0: ターゲット「インターネットゲートウェイ」（外部インターネットへの通信）

2. インターネットゲートウェイ (Internet Gateway)

- 概要: VPC内のAWSリソースとインターネットを接続するゲートウェイ。自動でスケールし、高可用性を提供。
- 設定: サブネットのルートテーブルに設定することで、インターネットアクセスが可能となる。
- パブリックサブネット: インターネットゲートウェイに接続されており、インターネットアクセス可能。
- プライベートサブネット: デフォルトではインターネットゲートウェイに接続されておらず、インターネットアクセス不可。

3. NATゲートウェイ (NAT Gateway)

- 概要: プライベートサブネット内のリソースがインターネットに接続できるようにするために使用。アウトバウンド接続は可能だが、インバウンド接続は不可。
- 設定: プライベートサブネットからインターネットへの通信を行うために、ルートテーブルで設定する。
- 例: 0.0.0.0/0: ターゲット「NAT Gateway」
- 自動スケール: 必要に応じて自動でスケーリングするため、可用性が高い。

4. ENI (Elastic Network Interface)

- 概要: 仮想ネットワークインターフェースで、EC2インスタンスにIPアドレスを割り当てる。
- EC2インスタンスにはデフォルトで1つのENIがアタッチされており、デタッチすることはできない。
- EC2インスタンスに複数のENIをアタッチすることができる（例えば、異なるSSL証明書をENIごとに割り当てて複数サイトを運用する場合）。
- ENIにはセキュリティグループを設定可能。

5. パブリックIPアドレス (Public IP Address)

- 概要: インターネットと通信できるIPアドレス。EC2インスタンスが終了または停止すると解放される。
- 特性: ランダムに割り当てられ、「パブリックIPv4アドレスの自動割り当て」を有効にしている場合、IPプールから自動的に割り当てられる。
- 問題点: EC2インスタンスのパブリックIPは可変であるため、セキュリティ制御の変更や外部アプリケーションとの通信設定に影響が出ることがある。

6. Elastic IPアドレス (EIP)

- 概要: 静的なインターネットIPアドレスで、EC2インスタンスに割り当てることで固定IPを提供する。
- 特性: EIPは料金が発生するが、パブリックIPに比べて可変ではないため、安定したインターネット接続が可能。
- 制限: 1つのEC2インスタンスには、Public IP Address または Elastic IP Address のいずれか一方しか割り当てることができない。

補足情報

- パブリックサブネット: インターネットに接続できるリソースを配置するためのサブネット。EC2インスタンスやALBなどが一般的に配置される。
- プライベートサブネット: インターネットから直接アクセスできないリソースを配置。セキュリティが高いデータベースなどが配置される。
- ルートテーブル: サブネットの通信先を決定するための設定。サブネット内のインスタンスがインターネットに接続するためには、インターネットゲートウェイまたはNATゲートウェイを経由するルートが必要。
