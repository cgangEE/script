set mouse=a
set nu
set history=4000
set backspace=2
set shiftwidth=4
set tabstop=4
set cindent
syntax on

func! R2()
	exec ":w"
	exec ":!clear&&g++ -g %<.cpp -o %< -lmysqlclient -I/usr/include/mysql/"
	exec "!./%<"
	endfunc

func! R()
		exec ":w"
	if &filetype == "cpp"
		exec "!clear&&g++ %<.cpp -o %<"
		exec "!./%<"
	elseif &filetype == "java"
		exec "!clear&&javac %"
		exec "!java %<"
	endif
endfunc

nnoremap <silent> <C-a> ggvG$"+y  
nnoremap <silent> <C-v> "+p  

noremap<F8> :call R2()<CR> 
noremap<F9> :call R()<CR>

let mapleader = ';'
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

iabbrev cg Gang Chen
inoremap jk <c-c>
