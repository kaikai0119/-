# dolphins
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dolphins - ホーム</title>
    <!-- CSSフレームワークの読み込み -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- カスタムCSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- ナビゲーションバー -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">動画共有プラットフォーム</a>
        <!-- 検索バー -->
        <form class="form-inline my-2 my-lg-0 ml-auto">
            <input class="form-control mr-sm-2" type="search" placeholder="動画を検索" aria-label="検索">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">検索</button>
        </form>
        <!-- ユーザーアカウント -->
        <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    ユーザー名
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">プロフィール</a>
                    <a class="dropdown-item" href="#">設定</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">ログアウト</a>
                </div>
            </li>
        </ul>
    </nav>

    <!-- メインコンテンツ -->
    <div class="container mt-4">
        <!-- ここに動画一覧やホームコンテンツを表示 -->
    </div>

    <!-- JavaScriptファイルの読み込み -->
    <script src="script.js"></script>
</body>
</html>
