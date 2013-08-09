_tt()
{
    local cur cword
    _init_completion || return

    if [[ $cword == 1 ]]; then
        COMPREPLY=( $( compgen -W '--start --stop --list' -- "$cur" ) )
    elif [[ $cword == 2 ]]; then
	COMPREPLY=( $( compgen -W '$(ls ~/.tt)' -- "$cur" ) )
    else
	echo
    fi

} &&
complete -F _tt tt
