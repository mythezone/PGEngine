Scene_Title.prototype.createBackground = function () {
    this._backSprite1 = new Sprite(
        ImageManager.loadPicture('Actor1_1')
    );
    this._backSprite2 = new Sprite(
        ImageManager.loadPicture('Actor1_2')
    );
    this._backSprites3 = new Sprite(
        ImageManager.loadPicture('Nature_3')
    );
    this.addChild(this._backSprite1);
    this.addChild(this._backSprite2);
    this.addChild(this._backSprites3);
    const gold_rect = new Rectangle(0, 0, 200, 150);
    this.createWindowLayer();
    this.gold = new Window_Gold(gold_rect);
    this.addWindow(this.gold);

    // bt = new Sprite_Button("menu");
    // bt.x = 200;
    // bt.y = 200;
    // bt.visible = true;
    // gr = new Rectangle(300, 300, 100, 100);
    // this.new_gr = new Window_Gold(gr);
    // this.addWindow(this.new_gr);
    // this.addWindow(bt);

    // this._mySprite = new Sprite(ImageManager.loadEnemy("Undine"));
    // this.addChild(this._mySprite);
    tmp_img = this.showImg('img/enemies/Zombie.png', 500, 300);
    this.addChild(tmp_img);

    w = new Window_Scrollable(new Rectangle(300, 300, 300, 100));
    w.drawText("Heloise\n核力量，发动机爱看，kdfjalkjfdlakjfk;ajfjdlakjfkleiojxfkadslj;fl\ndfan;lkfjaf", 0, 0, 300, 'center');
    this.addWindow(w);
};

Scene_Base.prototype.showImg = function (img_path, x = 0, y = 0) {
    temp_img = new Sprite(ImageManager.loadImg(img_path));
    temp_img.x = x;
    temp_img.y = y;
    return temp_img
}

ImageManager.loadImg = function (img_path) {
    if (img_path) {
        return this.loadBitmapFromUrl(img_path);
    } else {
        return this._emptyBitmap;
    }
};