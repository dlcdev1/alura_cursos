class Negociacao {
    constructor(_data, _quantidade, _valor) {
        this._data = _data;
        this._quantidade = _quantidade;
        this._valor = _valor;
    }
    get data() {
        return this._data;
    }
    get quantidade() {
        return this._quantidade;
    }
    get valor() {
        return this._valor;
    }
    // this._data = data;
    // this._quantidade = quantidade;
    // this._valor = valor;
    get volume() {
        return this._quantidade * this._valor;
    }
}
