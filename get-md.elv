use str

if (not-eq (count $args) (num 1)) {
    printf "Unexpected amount of arguments: Expecting 1, got %d\n" (count $args)
    exit 1
}

var unsplash_prefix = "https://unsplash.com/photos/"

var url = $args[0]
if (not (str:has-prefix $url $unsplash_prefix)) {
    printf "Expecting Unsplash URL starting with '%s', got '%s' instead.\n" $unsplash_prefix $url
    exit 1
}

var image_id = (str:trim-prefix $url $unsplash_prefix)
printf "Image ID: %s\n" $image_id

var client_id = "" # insert your client ID here

var api_call_url = (str:replace ":id" $image_id "https://api.unsplash.com/photos/:id")
var auth_header = (str:join "" ["Authorization: Client-ID " $client_id])
var curl_cmd = (str:join "" ['curl -f -H "' $auth_header '" ' $api_call_url])

var response = (eval $curl_cmd)
var json = (echo $response | from-json)

var author = $json[user][name]
var author_link = $json[user][links][html]
var image_description = $json[description]
var image_url = $json[links][html]
var image_hotlink = $json[urls][regular]

printf "Image author: %s (%s)\n" $author $author_link
printf "Image description: %s\n" $image_description
printf "Image original URL: %s\n" $image_url
printf "Hotlinking URL: %s\n" $image_hotlink

printf "\n------------------------------------\n\n"

var markdown = (printf "<center>![](%s)</center>\n\n<center><sub>%s. Photo by [%s](%s) on [Unsplash](%s).</sub></center>\n" ^
    $image_hotlink $image_description $author $author_link $image_url | slurp)

printf "Markdown:\n"
echo $markdown

echo $markdown | clip.exe
print "\nCopied to clipboard.\n\n"
