class Negociacoes {
    constructor() {
        this._negociacoes = [];
    }
    adicioana(negociacao) {
        this._negociacoes.push(negociacao);
    }
    paraArray() {
        return [].concat(this._negociacoes);
    }
}
